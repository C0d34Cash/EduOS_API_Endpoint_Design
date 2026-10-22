from fastapi import APIRouter
from uuid import UUID

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.get("/")
def list_roles():
    return {"message": "List-roles endpoint is ready.", "roles": []}


@router.post("/")
def create_role():
    return {"message": "Create-role endpoint is ready."}


@router.get("/{role_id}")
def get_role(role_id: UUID):
    return {
        "message": "Get-role endpoint is ready.",
        "role_id": role_id,
    }


@router.patch("/{role_id}")
def update_role(role_id: UUID):
    return {
        "message": "Update-role endpoint is ready.",
        "role_id": role_id,
    }


@router.delete("/{role_id}")
def deactivate_role(role_id: UUID):
    return {
        "message": "Deactivate-role endpoint is ready.",
        "role_id": role_id,
    }