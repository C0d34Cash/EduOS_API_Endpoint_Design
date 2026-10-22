from fastapi import APIRouter
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def list_users():
    return {"message": "List-users endpoint is ready.", "users": []}


@router.get("/{user_id}")
def get_user(user_id: UUID):
    return {
        "message": "Get-user endpoint is ready.",
        "user_id": user_id,
    }


@router.patch("/{user_id}")
def update_user(user_id: UUID):
    return {
        "message": "Update-user endpoint is ready.",
        "user_id": user_id,
    }


@router.delete("/{user_id}")
def deactivate_user(user_id: UUID):
    return {
        "message": "Deactivate-user endpoint is ready.",
        "user_id": user_id,
    }