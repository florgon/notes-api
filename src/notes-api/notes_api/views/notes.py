from typing import Union

from rest_framework.decorators import api_view
from rest_framework.response import Response

from web_services.api.error_code import ApiErrorCode
from web_services import (
    crud,
    serializers
)
from web_services.utils import (
    try_convert_type, validate_request
)
from web_services.api.response import (
    api_error, api_success
)


# Todo: Move this function away.
def try_query_note_from_request(request) -> Union[bool, Response]:
    """ Returns first boolean is OK or not, and note or error if failed to query. """
    # Validate request.
    is_valid, fields_or_error = validate_request(request, fields=["id"], auth_required=True)
    if not is_valid:
        return False, fields_or_error
    note_id, = fields_or_error

    # Validate note index value.
    note_id = try_convert_type(note_id, type=int)
    if note_id is None or note_id < 0:
        return False, api_error(ApiErrorCode.API_FIELD_INVALID, "`id` field has invalid format, expected a number!", {"field": "id"})
    
    # Query note from CRUD API.
    note = crud.notes.get_note_by_id(note_id)
    if not note:
        return False, api_error(ApiErrorCode.NOTE_NOT_EXISTS, "Note not found!")

    # Checking privacy.
    if not crud.notes.user_is_note_author(note, request.user):
        return False, api_error(ApiErrorCode.PRIVACY_PRIVATE_NOTE, "You are not allowed to delete this note.", {"description": "This note belongs to another user, which you dont have access to by privacy reasons!"})

    # Return note.
    return True, note


# Specific note methods.
@api_view(["GET"])
def get_note(request):
    """ Returns information about specific note by it`s ID. """

    # Validate request.
    is_valid, note_or_error = try_query_note_from_request(request)
    if not is_valid:
        return note_or_error
    note = note_or_error

    # Returning OK.
    return api_success(serializers.note.serialize(note))


@api_view(["GET"])
def delete_note(request):
    """ Deletes specific note by it`s ID and returns information about it. """

    # Validate request.
    is_valid, note_or_error = try_query_note_from_request(request)
    if not is_valid:
        return note_or_error
    note = note_or_error

    # Save note dict before delete request.
    note_dict = serializers.note.serialize(note)

    # Delete note.
    note.delete()

    # Returning OK with deleted note data.
    return api_success(note_dict)


@api_view(["GET"])
def edit_note(request):
    """ Updates information for specific note by it`s ID and given new information. Also returns information about it after editing. """

    # Validating request.
    is_valid, fields_or_error = validate_request(request, fields=["id", "text"], auth_required=True)
    if not is_valid:
        return fields_or_error
    note_id, text = fields_or_error

    # Validating note index value.
    note_id = try_convert_type(note_id, type=int)
    if note_id is None or note_id < 0:
        return api_error(ApiErrorCode.API_FIELD_INVALID, "`id` field has invalid format, expected a number!", {"field": "id"})
    
    # Query note from CRUD API.
    note = crud.notes.get_note_by_id(note_id)
    if not note:
        return api_error(ApiErrorCode.NOTE_NOT_EXISTS, "Note not found!")

    # Check privacy.
    if not crud.notes.user_is_note_author(note, request.user):
        return api_error(ApiErrorCode.PRIVACY_PRIVATE_NOTE, "You are not allowed to edit this note.", {"description": "This note belongs to another user, which you dont have access to by privacy reasons!"})

    # Edit note.
    note.update_text(text)
    note.save()

    # Returning OK.
    return api_success(serializers.note.serialize(note))


@api_view(["GET"])
def pin_note(request):
    """ Pins note for sorting and returns information about it. """

    # Validate request.
    is_valid, note_or_error = try_query_note_from_request(request)
    if not is_valid:
        return note_or_error
    note = note_or_error

    # Pin note.
    note.is_pinned = True
    note.save()

    # Returning OK with note data.
    return api_success(serializers.note.serialize(note))

@api_view(["GET"])
def unpin_note(request):
    """ Unpins note for sorting and returns information about it. """

    # Validate request.
    is_valid, note_or_error = try_query_note_from_request(request)
    if not is_valid:
        return note_or_error
    note = note_or_error

    # Unpin note.
    note.is_pinned = False
    note.save()

    # Returning OK with note data.
    return api_success(serializers.note.serialize(note))


# Base notes methods.


@api_view(["GET"])
def create_note(request):
    """ Creates new note with given parameters and returns information about it. """
    
    # Validating request.
    is_valid, fields_or_error = validate_request(request, fields=["text"], auth_required=True)
    if not is_valid:
        return fields_or_error
    text, = fields_or_error
   
    # Returning note from CRUD API.
    note = crud.notes.create_note(text, request.user)
    return api_success(serializers.note.serialize(note))


# Overall notes methods.

@api_view(["GET"])
def list_notes(request):
    """ Returns a list with notes (with information) of current authenticated user. """

    # Validating request.
    is_valid, fields_or_error = validate_request(request, auth_required=True)
    if not is_valid:
        return fields_or_error

    # Returning notes from CRUD API.
    notes = crud.notes.get_notes_from_user(request.user.id)
    return api_success(serializers.note.serialize_list(notes))



@api_view(["GET"])
def get_notes_counters(request):
    """ Returns counters (numbers) for notes data (like total notes count). """

    # Validating request.
    is_valid, fields_or_error = validate_request(request, auth_required=True)
    if not is_valid:
        return fields_or_error

    # Returning counters from CRUD API.
    notes_count = crud.notes.get_notes_count_for_user()
    return api_success({
        "counters": {"notes": {"total": notes_count}}
    })