from rest_framework.decorators import api_view

from web_services.api.response import api_success


@api_view(["GET"])
def get_routes_api(_):
    """Returns list of all routes releated to this app root API."""
    routes = [
        "/notes/",
        "/auth/",
        "/changelog"
    ]
    return api_success({"methods": {"api": routes}})


@api_view(["GET"])
def get_routes(_):
    """Returns list of all routes releated to this app APIs."""
    routes = [
        "/api/"
    ]
    return api_success({"methods": routes})