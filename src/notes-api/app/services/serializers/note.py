"""
    Note database model serializer.
"""

def _serialize(note):
    return {
        "id": note.id,
        "text": note.text,
        "created_at": note.time_created,
        "updated_at": note.time_updated
    }

def serialize(note):
    """Returns dict object for API response with serialized note data."""
    return {
        "note": _serialize(note)
    }

def serialize_list(notes: list):
    """Returns dict object for API response with serialized note data."""
    return {
        "notes": [
            _serialize(note) for note in notes
        ]
    }

serialize_notes = serialize_list
serialize_note = serialize