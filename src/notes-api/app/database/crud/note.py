"""
    Note CRUD utils for the database.
"""

# Libraries.
from sqlalchemy.orm import Session

# Services.
from app.database.models.note import Note


def get_by_workspace_id(db: Session, workspace_id: int) -> list[Note]:
    """ Returns note by it`s workspace ID. """
    return db.query(Note).filter(Note.workspace_id == workspace_id).all()


def get_by_id(db: Session, note_id: int) -> Note:
    """ Returns note by it`s ID. """
    return db.query(Note).filter(Note.id == note_id).first()


def create(db: Session, workspace_id: int, text: str) -> Note:
    """Creates Note"""

    # Create new note.
    note = Note(workspace_id=workspace_id, text=text)

    # Apply note in database.
    db.add(note)
    db.commit()
    db.refresh(note)

    return note