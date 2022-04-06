from typing import Optional

from rest_framework.authtoken.models import Token


def get_token_by_key(key: str) -> Optional[Token]:
    """ Returns a token by its key or None if not found. """
    try:
        token = Token.objects.select_related('user').get(key=key)
        return token
    except Token.DoesNotExist:
        return None

    