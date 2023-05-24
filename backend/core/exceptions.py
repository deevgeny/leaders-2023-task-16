from rest_framework.exceptions import APIException, NotFound, PermissionDenied


class NotFoundException(NotFound):
    ...


class PermissionDeniedException(PermissionDenied):
    ...


class InvalidFormatException(APIException):
    status_code = 400
    default_detail = "Invalid input format"
    default_code = "invalid_format"


class AlreadyExistsException(APIException):
    status_code = 409
    default_detail = "Entity with given data already exists"
    default_code = "already_exists"


class IntegrityBreachException(APIException):
    status_code = 409
    default_detail = "Entity integrity breach error"
    default_code = "integrity_breach"
