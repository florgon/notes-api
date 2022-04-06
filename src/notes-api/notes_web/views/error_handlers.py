from rest_framework.decorators import api_view

from web_services.api.error_code import ApiErrorCode
from web_services.api.response import api_error


@api_view(["GET"])
def handler404(*args, **kwargs):
    """Handles 404 error if not debug mode. """
    return api_error(ApiErrorCode.API_METHOD_NOT_FOUND, "Requested method does not exists.")
    

@api_view(["GET"])
def handler500(*args, **kwargs):
    """Handles 500 error if not debug mode. """
    return api_error(ApiErrorCode.SERVER_IS_DOWN, "Internal server error.")