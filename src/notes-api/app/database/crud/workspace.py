"""
    Workspace CRUD utils for the database.
"""

# Libraries.
from sqlalchemy.orm import Session

# Services.
from app.database.models.workspace import Workspace


def get_by_owner_id(db: Session, owner_id: int) -> list[Workspace]:
    """ Returns workspaces by it`s owner ID. """
    return db.query(Workspace).filter(Workspace.owner_id == owner_id).all()


def get_by_id(db: Session, workspace_id: int) -> Workspace:
    """ Returns workspace by it`s ID. """
    return db.query(Workspace).filter(Workspace.id == workspace_id).first()


def create(db: Session, owner_id: int, title: str) -> Workspace:
    """Creates Workspace"""

    # Create new workspace.
    workspace = Workspace(owner_id=owner_id, title=title)

    # Apply workspace in database.
    db.add(workspace)
    db.commit()
    db.refresh(workspace)

    return workspace