from rest_framework.exceptions import APIException, NotFound, PermissionDenied


class NotFoundException(NotFound):
    ...


class PermissionDeniedException(PermissionDenied):
    ...


class AlreadyExistsException(APIException):
    status_code = 409
    default_detail = 'Entity with given data already exists'
    default_code = 'already_exists'
