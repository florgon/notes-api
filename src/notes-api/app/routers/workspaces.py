
"""
    Workspaces API router.
    Provides API methods (routes) for working workspace.
"""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.services.request import query_auth_data_from_request, Request
from app.services.api.response import api_success
from app.services.serializers.workspace import serialize_workspace, serialize_workspaces
from app.database import crud
from app.database.dependencies import Session, get_db

router = APIRouter()


@router.get("/workspaces.get")
async def method_workspaces_get(req: Request, db: Session = Depends(get_db)) -> JSONResponse:
    """ Returns list of your workspace. """
    auth_data = query_auth_data_from_request(req)

    workspaces = crud.workspace.get_by_owner_id(db, auth_data.user_id)
    return api_success(serialize_workspaces(workspaces))


@router.get("/workspaces.new")
async def method_workspaces_new(req: Request, title: str, db: Session = Depends(get_db)) -> JSONResponse:
    """ Creates a new workspace. """
    auth_data = query_auth_data_from_request(req)

    workspace = crud.workspace.create(db, auth_data.user_id, title)
    return api_success(serialize_workspace(workspace))
