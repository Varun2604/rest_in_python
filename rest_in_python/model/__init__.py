
from ..view import RestView

class RestModel(object):

    def __init__(self, conn_holder):
        self.view = RestView(self, conn_holder)
        self.path = None
        self.name = None

    def getView(self):
        if self.view is None:
            raise NotImplemented
        return self.view

    def getPath(self):
        if self.path is None:
            raise NotImplemented
        return self.path

    def getName(self):
        if self.name is None:
            raise NotImplemented
        return self.name

