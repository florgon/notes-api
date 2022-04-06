from enum import Enum

class ApiErrorCode(Enum):
    """ API Standartized error codes. """

    # Auth releated.
    AUTH_REQUIRED = 0, 401
    AUTH_INVALID_CREDENTIALS = 1, 400
    AUTH_PASSWORDS_NOT_SAME = 2, 400,
    AUTH_EMAIL_TAKEN = 3, 400
    AUTH_USERNAME_TAKEN = 4, 400
    AUTH_SERVICE_ERROR = 5, 400
    AUTH_SERVICE_ACCOUNT_TAKEN = 6, 400

    # Non existance releated.
    NOTE_NOT_EXISTS = 10, 404

    # API related.
    API_FIELD_REQUIRED = 20, 400
    API_FIELD_INVALID = 21, 400
    API_METHOD_NOT_FOUND = 22, 404
    API_FORBIDDEN = 23, 403

    # Privacy releate.
    PRIVACY_PRIVATE_NOTE = 30, 403

    # Other.
    NOT_IMPLEMENTED = 50, 501
    SERVER_IS_DOWN = 51, 500