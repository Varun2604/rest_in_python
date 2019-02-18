import json

from ..exceptions import InvalidInput

class RestBean(object):

    #param  1. schema - the orm schema representation for the bean
    #       2. json_str - the json string (input in case of post, put)
    #       3. input - input in case of get, post, put
    #       4. id - id in case of get or partial bean
    def __init__(self, model, json_str=None, input=None, id=None):

        self.model = model
        if json_str is not None:
            self.input = json.load(json_str)
        elif input is not None and type(input) is dict:
            self.input = input
            self.is_partial = False

        if id is not None and self.input is None:
            self.is_partial = True

    #TODO 1.  implementation should return a new RestBean of the relation, if field is a relation field
    #TODO 2.   do a db fetch in case the object is a partial object
    def get(self, field):
        return getattr(self.input, field)

    def put(self, field, value):
        setattr(self.input, field, value)

    def get_keys(self):
        return self.input.keys()

    def get_schema(self):
        return self.model

