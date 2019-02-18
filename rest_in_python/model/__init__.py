
from ..view import RestView

class RestModel(object):

    def __init__(self):
        self.view = RestView(self)

    def getView(self):
        return self.view

