from fastapi import APIRouter, status
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

router = APIRouter(prefix="/auth", tags=["Authentication"])


class RegisterRequest(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)
    institution_id: UUID


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(data: RegisterRequest):
    return {
        "message": "Registration endpoint is ready.",
        "email": data.email,
        "username": data.username,
        "institution_id": data.institution_id,
        "status": "PENDING_VERIFICATION",
    }


@router.post("/login")
def login_user(data: LoginRequest):
    return {
        "message": "Login endpoint is ready.",
        "access_token": "temporary-access-token",
        "refresh_token": "temporary-refresh-token",
        "token_type": "bearer",
    }


@router.post("/refresh")
def refresh_access_token(data: RefreshTokenRequest):
    return {
        "message": "Refresh-token endpoint is ready.",
        "access_token": "new-temporary-access-token",
        "token_type": "bearer",
    }


@router.post("/logout")
def logout_user():
    return {"message": "Logout endpoint is ready."}


@router.get("/me")
def get_current_user():
    return {
        "message": "Current-user endpoint is ready.",
        "user": None,
    }