from logging import Logger
from typing import Optional, Tuple

from sqlalchemy import Result, Select, select
from sqlalchemy.orm import Session

from common.domain import (
    entities as common_entities,
    enums as common_enums,
    repositories as common_repositories,
)
from common.infrastructure.database import models as common_database_models
from common.infrastructure.database.models.auth import UserExtensionist
from common.infrastructure.logging.config import get_logger
from common.infrastructure.repositories import (
    postgresql as common_postgresql_repositories,
)


_LOGGER: Logger = get_logger(__name__)


class PostgreSQLAuthenticationRepository(
    common_postgresql_repositories.BasePostgreSQLRepository[
        common_entities.AuthenticatedUser, UserExtensionist
    ],
    common_repositories.AuthenticationRepository,
):
    """
    PostgreSQL implementation for AUTHENTICATION operations using modern SQLAlchemy 2.0+ style.

    Focused only on authentication concerns with select() statements.
    """

    def __init__(self, session: Session) -> None:
        super().__init__(session, UserExtensionist)

    def find_active_user_by_id(
        self, user_id: int
    ) -> Optional[common_entities.AuthenticatedUser]:
        """Find active user for authentication using select()."""
        _LOGGER.info(f"Finding active user for authentication: [{user_id}]")

        stmt: Select[Tuple[UserExtensionist]] = select(
            UserExtensionist
        ).where(
            UserExtensionist.id == user_id,
            UserExtensionist.is_active
            == common_enums.UserStatus.ACTIVE,
        )

        result: Result[Tuple[UserExtensionist]] = self._session.execute(
            stmt
        )
        user_model: UserExtensionist | None = (
            result.scalar_one_or_none()
        )

        if not user_model:
            _LOGGER.info(f"User with ID [{user_id}] not found or not active")
            return None

        return self._to_domain_entity(model=user_model)

    def _to_domain_entity(
        self, model: UserExtensionist
    ) -> common_entities.AuthenticatedUser:
        _LOGGER.info(f"Converting UserModel to AuthenticatedUser: [{model.id}]")
        user_status = (
            common_enums.UserStatus.ACTIVE
            if model.is_active
            else common_enums.UserStatus.INACTIVE
        )
        return common_entities.AuthenticatedUser(
            email=model.email,
            user_status=user_status,
            created_at=model.created_at,
            updated_at=model.updated_at,
            last_login=model.updated_at,  # Assuming last login is the last update
            id=model.id,
            is_premium=False,  # Assuming not premium
        )

    def _to_database_model(
        self, entity: common_entities.AuthenticatedUser
    ) -> UserExtensionist:
        """
        Convert authentication entity to database model.
        """
        raise NotImplementedError(
            "Cannot convert AuthenticatedUser to complete UserModel. "
            "Use specific update methods instead."
        )
