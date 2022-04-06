from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from auth_api.models import User

from web_services.api.error_code import ApiErrorCode
from web_services import (
    crud, 
    serializers, 
    mail
)
from web_services.api.response import (
    api_success, 
    api_error
)
from web_services.utils import (
    validate_email, 
    validate_request
)


@api_view(["GET"])
def sign_up(request):
    """Register new account for user. """

    # Validate request.
    is_valid, fields_or_error = validate_request(request, fields=["username", "email", "password", "password_confirmation"], auth_required=False)
    if not is_valid:
        return fields_or_error
    username, email, password, password_confirmation  = fields_or_error

    # Validate username.
    if len(username) < 4:
        return api_error(ApiErrorCode.API_FIELD_INVALID, "`username` field has invalid format, too short!", {"field": "username"})
    if username != username.lower():
        return api_error(ApiErrorCode.API_FIELD_INVALID, "`username` field has invalid format, only lowercase!", {"field": "username"})
    if crud.user.user_username_taken(username):
        return api_error(ApiErrorCode.AUTH_USERNAME_TAKEN, "Given username is already taken!")

    # Validate email.
    if not validate_email(email):
        return api_error(ApiErrorCode.API_FIELD_INVALID, f"`email` field has invalid format, email invalid! {email}", {"field": "email"})
    if crud.user.user_email_taken(email):
        return api_error(ApiErrorCode.AUTH_EMAIL_TAKEN, "Given email is already taken!")

    # Validate password.
    if not password_confirmation:
        return api_error(ApiErrorCode.API_FIELD_REQUIRED, "`password_confirmation` field is required!", {"field": "password_confirmation"})
    if password != password_confirmation:
        return api_error(ApiErrorCode.AUTH_PASSWORDS_NOT_SAME, "Password and it`s confirmation not the same!")
    if len(password) < 8:
        return api_error(ApiErrorCode.API_FIELD_INVALID, "`password` field has invalid format, too short!", {"field": "password"})

    # Create new user.
    user = User.objects.create_user(username, email, password)

    # Query fresh new token.
    token, is_new = Token.objects.get_or_create(user=user)
    
    # Email user.
    mail.send_signup_message(email=email, username=username)

    # Returning user index and token to login immediatly.
    return api_success({
        **serializers.token.serialize(token.key, is_new),
        "user_id": user.id
    })
    

@api_view(["GET"])
def resolve_auth_token(request):
    """Returns information about token (user, actually). Resolving token. """

    # Validate request.
    is_valid, fields_or_error = validate_request(request, fields=["token"], auth_required=False)
    if not is_valid:
        return fields_or_error
    key,  = fields_or_error

    # Query token.
    token, is_new = crud.token.get_token_by_key(key), False
    if not token:
        return api_error(ApiErrorCode.AUTH_INVALID_CREDENTIALS, "Token does not exist.")

    # Check that owner of the token is active.
    if not token.user.is_active:
        return api_error(ApiErrorCode.AUTH_INVALID_CREDENTIALS, "Owner of this token is not active or deleted!")

    # Returning user with token.
    return api_success({
        **serializers.token.serialize(token.key, is_new),
        **serializers.user.serialize(token.user)
    })


@api_view(["GET"])
def get_auth_token(request):
    """Returns authentication token by given username and password pair. Used as auth endpoint. """

    # Validate request.
    is_valid, fields_or_error = validate_request(request, fields=["username", "password"], auth_required=False)
    if not is_valid:
        return fields_or_error
    username, password = fields_or_error

    # Try authenticate user.
    user = authenticate(request=request, username=username, password=password)
    if not user:
        return  api_error(ApiErrorCode.AUTH_INVALID_CREDENTIALS, "Invalid credentials to autheticate!")

    # Try query token.
    token, is_new = Token.objects.get_or_create(user=user)
    if not token:
         return api_error(ApiErrorCode.AUTH_INVALID_CREDENTIALS, "Failed to create new token!")

    # Returning token.
    return api_success({
        **serializers.token.serialize(token.key, is_new),
        'user_id': user.id
    })