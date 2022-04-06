from typing import Optional

from auth_api.models import User


def user_username_taken(username: str) -> bool:
    """ Returns is given username already taken or not. """
    if User.objects.filter(username=username).exists():
        return True
    
    return False


def user_email_taken(email: str) -> bool:
    """ Returns is given email already taken or not. """
    if User.objects.filter(email=email).exists():
        return True
    
    return False


def get_user_by_vk_user_id(vk_user_id: str) -> Optional[User]:
    """ Returns a user by its VK user index or None if not found. """
    try:
        user = User.objects.get(vk_user_id=vk_user_id)
        return user
    except User.DoesNotExist:
        return None