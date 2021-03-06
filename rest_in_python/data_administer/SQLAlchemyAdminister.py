from ..data_administer import DataAdminister

#class has methods to fetch from
class SQLAlchemyAdminister(object):

    # param - model - the model for which the query is to be made
    # param - pk - long/int pk of the entry
    # return - model instance of the entry
    @staticmethod
    def get_entry(connection, model, pk):
        return model.query.filter_by(id=pk).first()

    # param - model - the model for which the query is to be made
    # param - list_info - dict containing query attributes like limit, search, sort, etc
    # return - array of model instances
    @staticmethod
    def get_list(connection, model, list_info):
        #TODO parse and use the list_info
        return model.query.all()

    # param - model - the model for which the query is to be made
    # param - input - model instance containing all the data to be inserted
    # return - updated model instance
    @staticmethod
    def add_entry(connection, model, input):
        datum = SQLAlchemyAdminister.json_to_model(model, input)
        connection.session.add(datum)
        connection.session.commit()
        return datum

    # param - model - the model for which the query is to be made
    # param - input - model instance containing all the data to be inserted
    # param - pk - long/int pk of the entry
    # return - updated model instance
    @staticmethod
    def edit_entry(connection, model, pk, datum):
        #TODO set the pk of datum to the given pk
        connection.session.add(datum)
        connection.session.commit()
        return datum

    # param - model - the model for which the query is to be made
    # param - pk - long/int pk of the entry
    # return - boolean True if successful delete
    @staticmethod
    def delete_entry(connection, model, pk):
        datum = SQLAlchemyAdminister.get_entry(connection, model=model, pk=pk)
        connection.session.delete(datum)
        connection.session.commit()
        return True

    @staticmethod
    def json_to_model(model, datum):
        columns = SQLAlchemyAdminister.get_columns_for_model(model)
        for c in columns:
            if c in datum and c != 'id':
                setattr(model, c, datum[c])
        return model

    @staticmethod
    #TODO implementation changes according to the underlying ORM, so use a function from the ORM util.
    def get_columns_for_model(schema):
        return schema.__table__.columns._data.keys()

