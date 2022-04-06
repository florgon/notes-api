from typing import Dict, Optional

from rest_framework.response import Response

from web_services.api.error_code import ApiErrorCode
from web_services.api.version import API_VERSION


def api_error(api_code: ApiErrorCode, message: str="", data: Optional[Dict] = None) -> Response:
    """Returns API error response. """
    if data is None:
        data = dict()

    code, status = api_code.value
    return Response({
        "api_version": API_VERSION,
        "error": {
            **{"message": message, "code": code, "status": status}, 
            **data
        }
    }, status=status)


def api_success(data: Dict) -> Response:
    """Returns success API response."""
    return Response({
        "api_version": API_VERSION,
        "success": {
            **data
        }
    }, status=200)
