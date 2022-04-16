from rest_framework.decorators import api_view

from web_services.api.response import api_success


@api_view(["GET"])
def get_routes(_):
    """Returns list of all routes releated to this API."""
    routes = [
        "/token/",
        "/signup",
    ]
    return api_success({"methods": {"api": {"auth": routes}}})


@api_view(["GET"])
def get_routes_token(_):
    """Returns list of all routes releated to this API for token."""
    routes = [
        "/get", "/resolve"
    ]
    return api_success({"methods": {"api": {"auth": {"token": routes}}}})
