"""
    Note CRUD utils for the database.
"""

# Libraries.
from sqlalchemy.orm import Session

# Services.
from app.database.models.note import Note
from app.services.api.errors import ApiErrorCode, ApiErrorException

def get_by_workspace_id(db: Session, workspace_id: int) -> list[Note]:
    """ Returns note by it`s workspace ID. """
    return db.query(Note).filter(Note.workspace_id == workspace_id).all()


def get_by_id(db: Session, note_id: int, *, _fail_fast: bool = True) -> Note:
    """ Returns note by it`s ID. """
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note and _fail_fast:
        raise ApiErrorException(ApiErrorCode.NOTE_NOT_FOUND, "Note does not exists!")
    return note



def create(db: Session, workspace_id: int, text: str) -> Note:
    """Creates Note"""

    # Create new note.
    note = Note(workspace_id=workspace_id, text=text)

    # Apply note in database.
    db.add(note)
    db.commit()
    db.refresh(note)

    return note