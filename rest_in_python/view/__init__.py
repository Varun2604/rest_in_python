from flask.views import MethodView
from flask import request

from ..bean import RestBean
from ..data_administer.SQLAlchemyAdminister import SQLAlchemyAdminister
from ..exceptions import RestException
from ..utils import get_as_response

HTTP_OPERATION = {
    'POST' : 'POST',
    'GET' : 'GET',
    'PUT' : 'PUT',
    'DELETE' : 'DELETE'
}

class RestView(MethodView):

    def __init__(self, model, conn_holder):
        # model is the Schema class instance of any orm (like DeclarativeBase instance in SQLAlchemy)
        self.model = model
        self.conn_holder = conn_holder

    def get(self, id=None):
        try:
            if id is not None:
                this_bean = self.process_data(id=id, method=HTTP_OPERATION['GET'])

                self.check_authorization(HTTP_OPERATION['GET'], this_bean, None)

                return get_as_response(this_bean.json())
            else:

                this_bean = self.process_data(input=request.json, method=HTTP_OPERATION['GET'])

                self.check_authorization(HTTP_OPERATION['GET'], this_bean, None)

                return get_as_response(this_bean.json())
        except Exception as e:
            print(e)
            return get_as_response({'message' : 'Unknown Error'}, False)

    def post(self):

        try:
            input_bean = RestBean(model=self.model, input=request.json)

            self.check_authorization(HTTP_OPERATION['POST'], input_bean, None)

            self.check_input_validation(input_bean, None)

            self.check_write_protection(input_bean, HTTP_OPERATION['POST'])

            input_bean = self.get_preprocessed_data(input_bean, HTTP_OPERATION['POST'])

            output = self.process_data(input=input_bean, method=HTTP_OPERATION['POST'])

            output = self.post_process_data(output, HTTP_OPERATION['POST'])

            return get_as_response(output.json())
        except Exception as e:
            print(e)
            return get_as_response({'message': 'Unknown Error'}, False)


    def delete(self, id):

        try:

            this_bean = self.get(id)

            self.check_authorization(HTTP_OPERATION['DELETE'], None, this_bean)

            self.check_write_protection(this_bean, HTTP_OPERATION['DELETE'])

            input_bean = self.get_preprocessed_data(this_bean, HTTP_OPERATION['DELETE'])

            self.process_data(input=input_bean, method=HTTP_OPERATION['DELETE'], id=id)

            self.post_process_data(None, HTTP_OPERATION['DELETE'])

            return get_as_response({'id' : id})
        except Exception as e:
            print(e)
            return get_as_response({'message': 'Unknown Error'}, False)

    def put(self, id):

        try:
            input_bean = RestBean(self.model, request.json)

            this_bean = self.get(id)

            self.check_authorization(HTTP_OPERATION['PUT'], input_bean, this_bean)

            self.check_input_validation(input_bean, this_bean)

            self.check_write_protection(input_bean, HTTP_OPERATION['PUT'])

            input_bean = self.get_preprocessed_data(input_bean, HTTP_OPERATION['PUT'])

            output = self.process_data(input=input_bean, method=HTTP_OPERATION['PUT'], id=id)

            output = self.post_process_data(output, HTTP_OPERATION['PUT'])

            return get_as_response(output.json())
        except Exception as e:
            print(e)
            return get_as_response({'message': 'Unknown Error'}, False)

    def get_model(self):
        if self.model is None:
            raise NotImplementedError('need to provide schema')

    def check_authorization(self, http_method, input_bean, old_bean):
        pass

    def check_input_validation(self, input_bean, old_bean):
        #TODO do field validation based on the field attributes taken from data_administer
        pass

    def validate_field(self, field, value):
        #TODO do field specific validation here
        pass

    def check_write_protection(self, input, method):
        pass

    def get_preprocessed_data(self, input, method):         # preprocess data before sending to db
        return input

    def process_data(self, method, input=None, id=None):                          # send to db and return new data/ fetch data from db
        conn = self.conn_holder.get_connection()
        if method == HTTP_OPERATION['POST']:
            output = SQLAlchemyAdminister.add_entry(conn, self.model(), input.input)
        elif method == HTTP_OPERATION['PUT']:
            output = SQLAlchemyAdminister.edit_entry(conn, self.model(), id, input.input)
        elif method == HTTP_OPERATION['DELETE']:
            output = SQLAlchemyAdminister.delete_entry(conn, self.model(), id)
        elif method == HTTP_OPERATION['GET'] and id is not None:
            output = SQLAlchemyAdminister.get_entry(conn, self.model, id)
        else:
            output = SQLAlchemyAdminister.get_list(conn, self.model, input)

        return RestBean(model=self.model, input=output)

    def post_process_data(self, input, method):                     # convert from model to python-dict or RestBean
        return input






