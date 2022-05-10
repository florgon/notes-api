from rest_framework.decorators import api_view

from web_services.api.response import api_success


@api_view(["GET"])
def get_routes(_):
    """Returns list of all routes releated to this API."""
    routes = [
        "/token/",
        "/service/",
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



@api_view(["GET"])
def get_routes_service(_):
    """Returns list of all routes releated to this API for services."""
    routes = [
        "/vk/"
    ]
    return api_success({"methods": {"api": {"auth": {"service": routes}}}})


@api_view(["GET"])
def get_routes_service_vk(_):
    """Returns list of all routes releated to this API for VK service."""
    routes = [
        "/request", "/callback", "/connect", "/disconnect"
    ]
    return api_success({"methods": {"api": {"auth": {"service": {"vk": routes}}}}})