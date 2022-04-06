def serialize(key, is_new):
    """ Returns dict for API response with token object"""
    return {
        "token": {
            "key": key,
            "is_new": is_new
        },
    }