"""
    Workspace CRUD utils for the database.
"""

# Libraries.
from sqlalchemy.orm import Session

# Services.
from app.database.models.workspace import Workspace
from app.services.api.errors import ApiErrorException, ApiErrorCode

def get_by_owner_id(db: Session, owner_id: int) -> list[Workspace]:
    """ Returns workspaces by it`s owner ID. """
    return db.query(Workspace).filter(Workspace.owner_id == owner_id).all()


def get_by_id(db: Session, workspace_id: int, *, _fail_fast: bool = True) -> Workspace:
    """ Returns workspace by it`s ID. """
    workspace = db.query(Workspace).filter(Workspace.id == workspace_id).first()
    if not workspace and _fail_fast:
        raise ApiErrorException(ApiErrorCode.WORKSPACE_NOT_FOUND, "Workspace does not exists!")
    return workspace

def create(db: Session, owner_id: int, title: str) -> Workspace:
    """Creates Workspace"""

    # Create new workspace.
    workspace = Workspace(owner_id=owner_id, title=title)

    # Apply workspace in database.
    db.add(workspace)
    db.commit()
    db.refresh(workspace)

    return workspace