"""
    Request handler and decoder.
    Allows to query auth data from your token or request.
    Root handler for authentication decode.
"""


from fastapi import Request
from requests import request, Response
from requests.exceptions import JSONDecodeError

from app.services.permissions import Permissions, Permission, parse_permissions_from_scope
from app.services.api.errors import ApiErrorCode, ApiErrorException


class AuthData(object):
    """ DTO for authenticated request."""
    user_id: int
    permissions: Permissions

    def __init__(self, user_id: int, permissions: Permissions) -> None:
        self.user_id = user_id
        self.permissions = permissions


def query_auth_data_from_token(token: str) -> AuthData:
    """
        Queries authentication data from your token.
        :param token: Token itself.
    """

    # Decode external token and query auth data from it.
    auth_data = _decode_token(token)
    return _query_auth_data(auth_data)


def query_auth_data_from_request(req: Request) -> AuthData:
    """
        Queries authentication data from request (from request token).
        :param req: Request itself.
    """

    # Get token from request and query data from it as external token.
    token = _get_token_from_request(req)
    return query_auth_data_from_token(token)


def _get_token_from_request(req: Request) -> str:
    """
        Returns token from request.
        :param req: Request itself.
    """
    return req.headers.get("Authorization") or req.query_params.get("access_token")


def _decode_token(token: str) -> Response:
    """
        Decodes given token, to it payload.
        :param token: Token to decode.
    """
    if not token:
        raise ApiErrorException(ApiErrorCode.AUTH_REQUIRED, "Auth required!")
    
    response = _check_token_with_sso_server(token)
    return response["success"]


def _query_scope_permissions(scope: str, required_permissions: Permissions | None) -> Permissions:
    """
        Queries scope permissions with checking required permission.
        :param scope: Scope string.
    """
    permissions = parse_permissions_from_scope(scope)

    if required_permissions:
        for required_permission in required_permissions:
            if required_permission not in permissions:
                raise ApiErrorException(
                    ApiErrorCode.AUTH_INSUFFICIENT_PERMISSSIONS, 
                    f"Insufficient permissions (required: {required_permission.value})", 
                    {"required_scope": required_permission.value})

    return permissions


def _check_token_with_sso_server(token: str) -> Response:
    """
        Checks that token is valid with SSO server.
        :param token: Token to check.
    """

    url = "https://api.florgon.space/secure.checkAccessToken"
    params = {"token": token}
    
    try:
        response = request("GET", url, params=params).json()
    except JSONDecodeError:
        raise ApiErrorException(
            ApiErrorCode.API_EXTERNAL_SERVER_ERROR, 
            "Unable to process your request due to server being down!"
        )
        
    _check_sso_server_response(response)
    return response


def _check_sso_server_response(response: Response) -> None:
    """
        Checks SSO server response to not contain any error.
        :param response: Response from SSO server.
    """
    if "error" in response:
        error_code = response["error"]["code"]
        error_message = response["error"]["message"]

        if error_code == 10 or error_code == 20: # AUTH_INVALID_TOKEN
            raise ApiErrorException(ApiErrorCode.AUTH_INVALID_TOKEN, error_message)

        if error_code == 11: #AUTH_EXPIRED_TOKEN
            raise ApiErrorException(ApiErrorCode.AUTH_EXPIRED_TOKEN, error_message)

        if error_code == 100: # USER_DEACTIVATED
            raise ApiErrorException(ApiErrorCode.USER_DEACTIVATED, error_message)

        raise ApiErrorException(ApiErrorCode.API_EXTERNAL_SERVER_ERROR, "Unable to process your request due to server being down (Or internal server error)!")


def _query_auth_data(response: Response) -> AuthData:
    """
        Queries authentication data from token payload.
        :param auth_data: Authentication data.
    """
    permissions = _query_scope_permissions(response.get("scope"), [Permission.notes])
    user_id = response.get("user_id")
    return AuthData(
        permissions=permissions,
        user_id=user_id
    )