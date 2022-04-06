from typing import Any, Callable, List, Tuple, Union, Dict
from django.core.validators import validate_email as django_validate_email
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from web_services.api.error_code import ApiErrorCode
from web_services.api.response import api_error


def validate_email(email: str) -> bool:
    """ Validates email and returns is valid or not. """
    try:
        django_validate_email(email)
        return True
    except ValidationError:
        return False


def try_convert_type(value: Any, *, type: Callable = int, default: Any=None) -> Any:
    """ Convert value to a given type or returns default value. """
    try:
        return type(value)
    except ValueError:
        return default


def validate_request(request, *, fields: List[str] = None, auth_required: bool=False) -> Tuple[bool, Union[Response, List[str]]]:
    """ Validates GET request and returns error response or list of GET fields. """
    return _validate_request(request, request.GET, fields=fields, auth_required=auth_required)


def validate_post_request(request, *, fields: List[str] = None, auth_required: bool=False) -> Tuple[bool, Union[Response, List[str]]]:
    """ Validates POST request and returns error response or list of POST fields. """
    return _validate_request(request, request.POST, fields=fields, auth_required=auth_required)


def _validate_request(request, fields_list: Dict, *, fields: List[str] = None, auth_required: bool=False) -> Tuple[bool, Union[Response, List[str]]]:
    """ Validates request and returns error response or list of fields. """

    if fields is None:
        fields = []

    # Auth check.
    if auth_required and not request.user.is_authenticated:
       return False, api_error(ApiErrorCode.AUTH_REQUIRED, "Authentication required!")
        
    field_values = []
    for field_name in fields:
        # Check value.
        field_value = fields_list.get(field_name, "")
        if not field_value:
            return False, api_error(ApiErrorCode.API_FIELD_REQUIRED, f"`{field_name}` field is required!", {"field": field_name})
        field_values.append(field_value)

    return True, field_values