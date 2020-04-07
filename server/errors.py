from werkzeug.exceptions import HTTPException


class BaseError(HTTPException):
    def __str__(self):
        return super().__str__() + ' (' + str(self.description) + ')'


class NotFoundError(BaseError):
    code = 404
    description = 'The requested object was not found'


class InternalServerError(BaseError):
    code = 500
    description = 'Sorry, something went wrong!'
