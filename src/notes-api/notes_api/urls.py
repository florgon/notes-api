from django.urls import path

from . import views


urlpatterns = [
    # Routes.
    path('api/notes', views.routes.get_routes),
    path('api/notes/upload', views.routes.get_routes_upload),
    path('api/notes/upload/server', views.routes.get_routes_upload_server),

    # Methods for specific note.
    path('api/notes/get', views.notes.get_note),
    path('api/notes/delete', views.notes.delete_note),
    path('api/notes/edit', views.notes.edit_note),
    path('api/notes/unpin', views.notes.unpin_note),
    path('api/notes/pin', views.notes.pin_note),

    # Other methods.
    path('api/notes/create', views.notes.create_note),

    # Total notes information getters.
    path('api/notes/list', views.notes.list_notes),
    path('api/notes/counters', views.notes.get_notes_counters),

    # Upload server.
    path('api/notes/upload/server/get', views.upload.get_upload_server),
]
