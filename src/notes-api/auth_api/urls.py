from django.urls import path

from . import views


urlpatterns = [
    # Routes.
    path('auth', views.routes.get_routes),
    path('auth/token', views.routes.get_routes_token),

    # Auth.
    path('auth/signup', views.auth.sign_up),
    # Token.
    path('auth/token/get', views.auth.get_auth_token),
    path('auth/token/resolve', views.auth.resolve_auth_token),
]