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

    # for both add and edit
    @staticmethod
    def json_to_model(model, datum):
        columns = ModelJsonConverters.get_columns_for_model(model)
        for c in columns:
            if c in datum and c != 'id':
                setattr(model, c, datum[c])
        return model

    @staticmethod
    #TODO implementation changes according to the underlying ORM, so use a function from the ORM util.
    def get_columns_for_model(schema):
        return schema.__table__.columns._data.keys()