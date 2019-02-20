from .model import RestModel

PATH_MODEL_MAP = {}
PATH_VIEW_MAP = {}

class ConnectionHolder(object):

    def __init__(self, conn):
        self.conn = conn

    def get_connection(self):
        return self.conn

def create_route_map(flask_app, *args):
    for model in args:
        if isinstance(model, RestModel):
            flask_app.add_url_rule('/'+model.getPath(), methods=["GET", "POST"],view_func=model.getView().as_view(model.getName(), model=model.__class__, conn_holder=model.view.conn_holder))
            flask_app.add_url_rule('/'+model.getPath()+'/<int:id>', methods=["GET", "PUT", "DELETE"],view_func=model.getView().as_view(model.getName()+'_idempotent', model=model.__class__, conn_holder=model.view.conn_holder))
            PATH_MODEL_MAP[model.getPath()] = model.__class__
            PATH_VIEW_MAP[model.getPath()] = model.getView()

def after_request(response):
    return response