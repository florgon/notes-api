from rest_framework.decorators import api_view

from web_services.api.response import api_success


@api_view(["GET"])
def get_routes(_):
    """ Returns list of all routes releated to this API. """
    routes = [
        "/get", "/delete",
        "/edit", "/create",
        "/list", "/counters",
        "/pin", "/unpin"
    ]
    return api_success({"methods": {"api": {"notes": routes}}})


@api_view(["GET"])
def get_routes_upload(_):
    """ Returns list of all routes releated to this API upload. """
    routes = [
        "/server/"
    ]
    return api_success({"methods": {"api": {"notes": {"upload": routes}}}})


@api_view(["GET"])
def get_routes_upload_server(_):
    """ Returns list of all routes releated to this API upload server. """
    routes = [
        "/get"
    ]
    return api_success({"methods": {"api": {"notes": {"upload": {"server": routes}}}}})