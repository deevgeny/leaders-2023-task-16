from rest_framework.exceptions import APIException


class NotFoundException(APIException):
    status_code = 404
    default_detail = 'Entity does not exist'
    default_code = 'not_found'


class AlreadyExistsException(APIException):
    status_code = 409
    default_detail = 'Entity with given data already exists'
    default_code = 'already_exists'
