from rest_framework.decorators import api_view

from web_services.api.error_code import ApiErrorCode
from web_services.api.response import (
    api_error
)


@api_view(["GET"])
def get_upload_server(_):
    """Returns upload server URL to upload your files that should be used in note context."""
    return api_error(ApiErrorCode.NOT_IMPLEMENTED, "Upload server not implemented yet!")