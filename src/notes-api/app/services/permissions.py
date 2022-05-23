from enum import Enum

class Permission(Enum):
    oauth_clients = "oauth_clients"
    email = "email"
    noexpire = "noexpire"
    edit = "edit"
    gatey = "gatey"
    notes = "notes"

Permissions: list[Permission] = list[Permission]  # Type hint.

def parse_permissions_from_scope(scope: str) -> Permissions:
    return list(set([
        Permission(permission) for permission in 
        scope.split(SCOPE_PERMISSION_SEPARATOR)
        if (permission and permission in SCOPE_ALLOWED_PERMISSIONS and permission)
    ]))


SCOPE_PERMISSION_SEPARATOR = ","
SCOPE_ALLOWED_PERMISSIONS = [permission.value for permission in [
    Permission.oauth_clients,
    Permission.email,
    Permission.noexpire,
    Permission.edit,
    Permission.gatey,
    Permission.notes
]]