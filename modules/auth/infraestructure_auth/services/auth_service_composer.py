from fastapi import Depends
from sqlalchemy.orm import Session

from modules.auth.application_auth.services.auth_service import AuthService
from modules.auth.infraestructure_auth.repositories.postgresql.auth_repository import (
    PostgreSQLAuthRepository,
)
from common.infrastructure.database.session import session_manager


def get_auth_service(
    session: Session = Depends(session_manager.get_session),
) -> AuthService:
    auth_repository = PostgreSQLAuthRepository(session=session)
    return AuthService(auth_repository=auth_repository)
