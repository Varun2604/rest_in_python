from app.models import Lead, Scheduled_Push_Message
from app import db
import json

api_model_map = {
    'leads' : Lead,
    'schedules' : Scheduled_Push_Message
}

def handle_api_call(entity, id, method, input=None):

    if entity not in api_model_map:
        raise ApiException('invalid entity')

    if method == 'POST' and input is None:
        raise ApiException('input data required')
    elif method == 'PUT' and input is None:
        raise ApiException('input data required')

    if method == 'GET':
        model = api_model_map[entity]
        if id is None:
            data = model.query.all()
            return ModelJsonConverters.model_list_to_json(model, data)

        else:
            datum = model.query.filter_by(id=id).first()
            return ModelJsonConverters.model_to_json(model, datum)

    elif method == 'POST':
        model = api_model_map[entity]
        datum = model()
        datum = ModelJsonConverters.json_to_model(datum, json.loads(input))
        db.session.add(datum)
        db.session.commit()
        # datum = model.query.filter_by(id=model.id).first()
        return ModelJsonConverters.model_to_json(model, datum)

    elif method == 'PUT':
        model = api_model_map[entity]
        datum = model.query.filter_by(id=id).first()
        if datum is None:
            raise ApiException('invalid id')
        datum = ModelJsonConverters.json_to_model(datum, json.loads(input))
        db.session.add(datum)
        db.session.commit()
        return ModelJsonConverters.model_to_json(model, datum)

    elif method == 'DELETE':
        model = api_model_map[entity]
        datum = model.query.filter_by(id=id).first()
        if datum is None:
            raise ApiException('invalid id')
        db.session.delete(datum)
        db.session.commit()
        return {'status': 'success'}

    else:
        raise ApiException('Invalid method')

class ApiException(BaseException):
    def __init__(self, *args, **kwargs):
        pass

class ModelJsonConverters(object):

    @staticmethod
    def model_to_json(model, datum, columns=None):
        if columns is None:
            columns = ModelJsonConverters.get_columns_for_model(model)
        json = {}
        for c in columns:
            json[c] = getattr(datum, c)
        return json

    @staticmethod
    def model_list_to_json(model, data):
        columns = ModelJsonConverters.get_columns_for_model(model)
        json_arr = []
        for datum in data:
            json_arr.append(ModelJsonConverters.model_to_json(model, datum, columns))
        return json_arr

    @staticmethod
    def json_to_model(model, datum):
        columns = ModelJsonConverters.get_columns_for_model(model)
        for c in columns:
            if c in datum and c != 'id':
                setattr(model, c, datum[c])
        return model

    @staticmethod
    def get_columns_for_model(model):
        return model.__table__.columns._data.keys()

