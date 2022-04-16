from django.urls import path

from . import views


urlpatterns = [
    # Routes.
    path('notes', views.routes.get_routes),
    path('notes/upload', views.routes.get_routes_upload),
    path('notes/upload/server', views.routes.get_routes_upload_server),

    # Methods for specific note.
    path('notes/get', views.notes.get_note),
    path('notes/delete', views.notes.delete_note),
    path('notes/edit', views.notes.edit_note),
    path('notes/unpin', views.notes.unpin_note),
    path('notes/pin', views.notes.pin_note),

    # Other methods.
    path('notes/create', views.notes.create_note),

    # Total notes information getters.
    path('notes/list', views.notes.list_notes),
    path('notes/counters', views.notes.get_notes_counters),

    # Upload server.
    path('notes/upload/server/get', views.upload.get_upload_server),
]
