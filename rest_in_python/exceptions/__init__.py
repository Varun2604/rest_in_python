class RestException(Exception):

    def __init__(self, code=4000, title='Internal Error', field=None, id=None, *args, **kwargs):
        message = title
        if kwargs is not None:
            if 'message' in kwargs:
                    message = kwargs['message']
        super(RestException, self).__init__(message=message, *args, **kwargs)
        self.code = code
        self.title = title
        self.field = field

class InvalidInput(RestException):

    def __init__(self, field=None):
        super(InvalidInput, self).__init__(code=4001, title='Invalid Input', field=field, message='Input object not provided')


REST_EXCEPTION_MAP = {
    InvalidInput : 4001
}