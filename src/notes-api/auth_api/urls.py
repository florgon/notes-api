from django.urls import path

from . import views


urlpatterns = [
    # Routes.
    path('api/auth', views.routes.get_routes),
    path('api/auth/token', views.routes.get_routes_token),
    path('api/auth/service', views.routes.get_routes_service),
    path('api/auth/service/vk', views.routes.get_routes_service_vk),

    # Auth.
    path('api/auth/signup', views.auth.sign_up),
    # Token.
    path('api/auth/token/get', views.auth.get_auth_token),
    path('api/auth/token/resolve', views.auth.resolve_auth_token),
    # Services.
    path('api/auth/service/vk/request', views.services.vk_request_auth),
    path('api/auth/service/vk/callback', views.services.vk_callback_auth),
    path('api/auth/service/vk/connect', views.services.vk_connect_auth),
    path('api/auth/service/vk/disconnect', views.services.vk_disconnect_auth)
]