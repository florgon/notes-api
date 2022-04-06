from typing import (
    List, Dict
)

from notes_api.models import Note


def serialize(note: Note) -> Dict:
    """Returns dict object for API response from note. """
    return {
            "note": {
                "id": note.id,
                "text": note.text,
                "updated_at": note.updated_at,
                "created_at": note.created_at,
                "author_id": note.author.id,
                "sorting": {
                    "is_pinned": note.is_pinned
                }
            }
        }

def serialize_list(notes: List[Note]) -> Dict:
    """Returns dict object for API response from notes list."""
    return {
        "notes": [serialize(note) for note in notes]
    }