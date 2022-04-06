def serialize(user):
    """Returns dict object for API response with serialized user data."""
    return {
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "services": {
                "vk": user.vk_user_id is not None
            }
        }
    }