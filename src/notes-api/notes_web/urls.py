from django.urls import path, include

from . import views


# Error handlers.
handler404 = views.error_handlers.handler404
handler500 = views.error_handlers.handler500


urlpatterns = [
    path('/changelog', views.changelog.get_api_changelog),
    path('/', views.routes.get_routes_api),
    
    path('', views.routes.get_routes),

    path('', include('notes_api.urls')),
    path('', include('auth_api.urls'))
]