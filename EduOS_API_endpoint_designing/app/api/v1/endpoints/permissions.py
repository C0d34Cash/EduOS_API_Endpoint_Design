from fastapi import APIRouter
from uuid import UUID

router = APIRouter(prefix="/permissions", tags=["Permissions"])


@router.get("/")
def list_permissions():
    return {
        "message": "List-permissions endpoint is ready.",
        "permissions": [],
    }


@router.post("/")
def create_permission():
    return {"message": "Create-permission endpoint is ready."}


@router.post("/roles/{role_id}")
def assign_permission_to_role(role_id: UUID):
    return {
        "message": "Assign-permission-to-role endpoint is ready.",
        "role_id": role_id,
    }


@router.delete("/roles/{role_id}/{permission_id}")
def remove_permission_from_role(role_id: UUID, permission_id: UUID):
    return {
        "message": "Remove-permission-from-role endpoint is ready.",
        "role_id": role_id,
        "permission_id": permission_id,
    }