# EduOS API Endpoint Design

A FastAPI-based endpoint design for the EduOS (Education Operating System) backend.

## Current Module

**Module 1 — Authentication & Identity Management**

Current endpoint groups:

- Authentication
- Users
- Roles
- Permissions
- Sessions

## Project Structure

```text
app/
├── main.py
└── api/
    └── v1/
        ├── api.py
        └── endpoints/
            ├── auth.py
            ├── users.py
            ├── roles.py
            ├── permissions.py
            └── sessions.py
