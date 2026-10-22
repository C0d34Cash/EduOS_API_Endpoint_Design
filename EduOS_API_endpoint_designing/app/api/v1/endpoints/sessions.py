from fastapi import APIRouter
from uuid import UUID

router = APIRouter(prefix="/sessions", tags=["Sessions"])


@router.get("/")
def list_my_sessions():
    return {
        "message": "List-active-sessions endpoint is ready.",
        "sessions": [],
    }


@router.delete("/{session_id}")
def revoke_session(session_id: UUID):
    return {
        "message": "Session-revoke endpoint is ready.",
        "session_id": session_id,
    }


@router.delete("/")
def revoke_all_other_sessions():
    return {"message": "All other sessions revoked."}