"""
    Workspace database model serializer.
"""

def _serialize(workspace):
    return {
        "id": workspace.id,
        "title": workspace.title
    }

def serialize(workspace):
    """Returns dict object for API response with serialized workspace data."""
    return {
        "workspace": _serialize(workspace)
    }

def serialize_list(workspaces: list):
    """Returns dict object for API response with serialized workspace data."""
    return {
        "workspaces": [
            _serialize(workspace) for workspace in workspaces
        ]
    }

serialize_workspaces = serialize_list
serialize_workspace = serialize