from flask.views import MethodView
from flask import request

from bean import RestBean
from data_administer import DB_OPERATIONS

class RestView(MethodView):

    def __init__(self, model):
        # model is the Schema class instance of any orm (like DeclarativeBase instance in SQLAlchemy)
        self.model = model

    def get(self, id):
        if id is None:
            # return a list of users
            pass
        else:
            # return a single user

            pass

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

    def get_model(self):
        if self.model is None:
            raise NotImplementedError('need to provide schema')

    def check_authorization(self):
        pass

    def check_input_validation(self, input):
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
        #1. pass the RestBean to beanModelCOnverter and fetch the modal
        #2. send model to data administer

        return input

    def post_process_data(self, input):                     # convert from model to python-dict or RestBean
        return input





