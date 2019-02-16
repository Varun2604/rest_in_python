
#interface to fetch data from the specified orm
# all methods throw exceptions.

DB_OPERATIONS = {
    'CREATE' : 'CREATE',
    'READ' : 'READ',
    'UPDATE' : 'UPDATE',
    'DELETE' : 'DELETE',
    'READ_LIST' : 'READ_LIST'
}
class DataAdminister(object):

    def __init__(self, db_connection):
        if db_connection is None:
            raise NotImplementedError('need db connnection instance')
        self.db_conn = db_connection

    # param - model - the model for which the query is to be made
    # param - pk - long/int pk of the entry
    # return - model instance of the entry
    def get_entry(self, model, pk):
        pass

    # param - model - the model for which the query is to be made
    # param - list_info - dict containing query attributes like limit, search, sort, etc
    # return - array of model instances
    def get_list(self, model, list_info):
        pass

    # param - model - the model for which the query is to be made
    # param - datum - model instance containing all the data to be inserted
    # return - updated model instance
    def add_entry(self, model, datum):
        pass

    # param - model - the model for which the query is to be made
    # param - datum - model instance containing all the data to be inserted
    # param - pk - long/int pk of the entry
    # return - updated model instance
    def edit_entry(self, model, pk, datum):
        pass

    # param - model - the model for which the query is to be made
    # param - pk - long/int pk of the entry
    # return - boolean True if successful delete
    def delete_entry(self, model, pk):
        pass

    #TODO add methods to get field properties for a particular model and a field.
