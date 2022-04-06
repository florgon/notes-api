from typing import Optional, List

from auth_api.models import User
from notes_api.models import Note


def get_notes_from_user(user_id: int) -> List[Note]:
    """ Returns list of user notes by its id. """
    return Note.objects.filter(author=user_id)
    

def get_notes_count_for_user(user_id: int) -> int:
    """ Returns number of notes of user by its id. """
    return Note.objects.filter(author=user_id).count()


def get_note_by_id(note_id: int) -> Optional[Note]:
    """ Returns a note by its id or None if not found. """
    try:
        return Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return None


def user_is_note_author(note: Note, user: User) -> bool:
    """ Returns is given user author of given note or no. """
    return note.author_id == user.id


def create_note(text: str, user: User) -> Note:
    """Creates new note and returns it."""
    return Note.objects.create(text=text, author=user)