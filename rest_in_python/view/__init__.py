from flask.views import MethodView
from flask import request

from ..bean import RestBean
from ..data_administer import DB_OPERATIONS,SQLAlchemyAdminister

class RestView(MethodView):

    def __init__(self, model):
        # model is the Schema class instance of any orm (like DeclarativeBase instance in SQLAlchemy)
        self.model = model
        self.data_administer = SQLAlchemyAdminister();

    def get(self, id):
        if id is None:
            # return a list of users
            pass
        else:
            # return a single user

            pass

    def post(self):

        input_bean = RestBean(self.model, request.json)

        self.check_authorization('POST', input_bean, None)

        self.check_input_validation(input_bean, None)

        self.check_write_protection(input_bean)

        input_bean = self.get_preprocessed_data(input_bean, "POST")

        output = self.process_data(input_bean, "POST")

        output = self.get_preprocessed_data(output, "POST")

        return output

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

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

    def check_write_protection(self, input):
        pass

    def get_preprocessed_data(self, input, method):         # preprocess data before sending to db
        return input

    def process_data(self, input, method):                          # send to db and return new data/ fetch data from db
        if method == 'POST':
            output = self.data_administer.add_entry(self.model, input)
        elif method == 'PUT':
            output = self.data_administer.edit_entry(self.model, input)
        elif method == 'DELETE':
            output = self.data_administer.delete_entry(self.model, input)
        elif method == 'GET' and isinstance(input, int):
            output = self.data_administer.get_entry(self.model, input)
        else:
            output = self.data_administer.get_list(self.model, input)

        return output

    def post_process_data(self, input):                     # convert from model to python-dict or RestBean
        return input






