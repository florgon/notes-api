
"""
    Notes API router.
    Provides API methods (routes) for working notes.
"""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.services.request import query_auth_data_from_request, Request
from app.services.api.response import api_success, api_error, ApiErrorCode
from app.services.serializers.note import serialize_notes, serialize_note
from app.database import crud
from app.database.dependencies import Session, get_db

router = APIRouter()


@router.get("/notes.get")
async def method_notes_get(req: Request, workspace_id: int, db: Session = Depends(get_db)) -> JSONResponse:
    """ Returns list of notes in workspace. """
    auth_data = query_auth_data_from_request(req)

    workspace = crud.workspace.get_by_id(db, workspace_id=workspace_id)
    if workspace.owner_id != auth_data.user_id:
        return api_error(ApiErrorCode.ACCESS_DENIED, "This item is not owned by you!")

    notes = crud.note.get_by_workspace_id(db, workspace_id=workspace_id)
    return api_success({
        "workspace_id": workspace_id,
        **serialize_notes(notes)
    })


@router.get("/notes.edit")
async def method_notes_edit(req: Request, text: str | None, note_id: int, db: Session = Depends(get_db)) -> JSONResponse:
    """ Edits note. """
    auth_data = query_auth_data_from_request(req)

    note = crud.note.get_by_id(db, note_id=note_id)
    workspace = crud.workspace.get_by_id(db, workspace_id=note.workspace_id)
    if workspace.owner_id != auth_data.user_id:
        return api_error(ApiErrorCode.ACCESS_DENIED, "This item is not owned by you!")
    
    is_changed = False
    if text and text != note.text:
        note.text = text
    if is_changed:
        db.commit()

    return api_success({
        "workspace_id": workspace.id,
        "is_changed": is_changed,
        **serialize_note(note)
    })


@router.get("/notes.delete")
async def method_notes_delete(req: Request, note_id: int, db: Session = Depends(get_db)) -> JSONResponse:
    """ Deletes note. """
    auth_data = query_auth_data_from_request(req)

    note = crud.note.get_by_id(db, note_id=note_id)
    workspace = crud.workspace.get_by_id(db, workspace_id=note.workspace_id)
    if workspace.owner_id != auth_data.user_id:
        return api_error(ApiErrorCode.ACCESS_DENIED, "This item is not owned by you!")

    serialized_note = serialize_note(note)
    db.delete(note)

    return api_success({
        "workspace_id": workspace.id,
        **serialized_note
    })


@router.get("/notes.new")
async def method_notes_new(req: Request, workspace_id: int, text: str, db: Session = Depends(get_db)) -> JSONResponse:
    """ Creates a new note. """
    auth_data = query_auth_data_from_request(req)

    workspace = crud.workspace.get_by_id(db, workspace_id=workspace_id)
    if workspace.owner_id != auth_data.user_id:
        return api_error(ApiErrorCode.ACCESS_DENIED, "This item is not owned by you!")
    note = crud.note.create(db, workspace_id, text)
    return api_success({
        "workspace_id": workspace_id,
        **serialize_note(note)
    })
