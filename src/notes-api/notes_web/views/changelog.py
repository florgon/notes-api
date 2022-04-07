from rest_framework.decorators import api_view

from web_services.api.response import api_success


@api_view(["GET"])
def get_api_changelog(_):
    """Returns list of all routes releated to this app APIs."""
    changelog = {
        "1.2.3": [
            "Dissalowed to connect external VK account to more than 1 account. (Now there will code 6 error raised)"
        ],
        "1.2.2": [
            "Add VK auth service (`/api/auth/service/vk`).",
            "`/api/auth/token/resolve` now returns services field which may be used for showing current service connectivity status"
        ],
        "1.1.2": [
            "Add `/api/changelog` method."
        ],
        "1.1.1": [
            "`/api/auth/token/resolve` now returns `email` field."
        ],
        "1.1": [
            "Note object now contains `sorting` field with `is_pinned` field, that is used for creating sorting system in clients.",
            "2 new methods `/api/note/pin` and `/api/note/unpin` that requires `id` of the note and switching them pinned state."
        ],
        "1.0": [
            "Initial release."
        ]
    }
    
    return api_success({"changelog": changelog})