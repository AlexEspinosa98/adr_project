from fastapi import Depends, HTTPException, Security, status, Query
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.infraestructure_auth.repositories.postgresql.auth_repository import (
    PostgreSQLAuthRepository,
)
from common.infrastructure.database.session import session_manager

api_key_header = APIKeyHeader(name="X-API-TOKEN", auto_error=False)


def get_current_user_from_token(
    api_key: str = Security(api_key_header),
    session: Session = Depends(session_manager.get_session),
) -> UserExtensionist:
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    repo = PostgreSQLAuthRepository(session)
    user = repo.get_user_by_token(token=api_key)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_user_from_query_token(
    api_token: str = Query(..., description="The API token of the user"),
    session: Session = Depends(session_manager.get_session),
) -> UserExtensionist:
    if not api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated, token is missing",
            headers={"WWW-Authenticate": "Bearer"},
        )

    repo = PostgreSQLAuthRepository(session)
    user = repo.get_user_by_token(token=api_token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
