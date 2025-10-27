from logging import Logger
from typing import Optional, Tuple

from sqlalchemy import Result, Select, select
from sqlalchemy.orm import Session

from common.infrastructure.repositories import (
    postgresql as common_postgresql_repositories,
)
from common.infrastructure.logging.config import get_logger

from modules.admin.domain_admin.repositories.admin_authentication_repository import AdminAuthenticationRepository as IAdminAuthenticationRepository
from modules.admin.domain_admin.entities.admin_user_entity import AdminUser as AdminUserEntity
from common.infrastructure.database.models.admin import AdminUser as AdminUserModel


_LOGGER: Logger = get_logger(__name__)


class AdminAuthenticationRepository(
    common_postgresql_repositories.BasePostgreSQLRepository[
        AdminUserEntity, AdminUserModel
    ],
    IAdminAuthenticationRepository,
):
    """
    PostgreSQL implementation for ADMIN AUTHENTICATION operations using modern SQLAlchemy 2.0+ style.

    Focused only on authentication concerns with select() statements.
    """

    def __init__(self, session: Session) -> None:
        super().__init__(session, AdminUserModel)

    def find_active_admin_user_by_id(
        self, user_id: int
    ) -> Optional[AdminUserEntity]:
        """Find active user for authentication using select()."""
        _LOGGER.info(f"Finding active admin user for authentication: [{user_id}]")

        stmt: Select[Tuple[AdminUserModel]] = select(
            AdminUserModel
        ).where(
            AdminUserModel.id == user_id,
            AdminUserModel.is_active == True,
        )

        result: Result[Tuple[AdminUserModel]] = self._session.execute(
            stmt
        )
        user_model: AdminUserModel | None = (
            result.scalar_one_or_none()
        )

        if not user_model:
            _LOGGER.info(f"Admin user with ID [{user_id}] not found or not active")
            return None

        return self._to_domain_entity(model=user_model)

    def find_admin_user_by_email_and_password(
        self, email: str, password: str
    ) -> Optional[AdminUserEntity]:
        """Find user by email and password for authentication."""
        _LOGGER.info(f"Finding admin user by email: [{email}]")

        stmt: Select[Tuple[AdminUserModel]] = select(
            AdminUserModel
        ).where(
            AdminUserModel.email == email,
            AdminUserModel.password == password, # Password should be hashed
            AdminUserModel.is_active == True,
        )

        result: Result[Tuple[AdminUserModel]] = self._session.execute(
            stmt
        )
        user_model: AdminUserModel | None = (
            result.scalar_one_or_none()
        )

        if not user_model:
            _LOGGER.info(f"Admin user with email [{email}] not found or not active")
            return None

        return self._to_domain_entity(model=user_model)

    def find_admin_user_by_email(self, email: str) -> Optional[AdminUserEntity]:
        """Find admin user by email."""
        _LOGGER.info(f"Finding admin user by email: [{email}]")

        stmt: Select[Tuple[AdminUserModel]] = select(AdminUserModel).where(
            AdminUserModel.email == email,
            AdminUserModel.is_active == True,
        )

        result: Result[Tuple[AdminUserModel]] = self._session.execute(stmt)
        user_model: AdminUserModel | None = result.scalar_one_or_none()

        if not user_model:
            _LOGGER.info(f"Admin user with email [{email}] not found or not active")
            return None

        return self._to_domain_entity(model=user_model)

    def find_admin_user_by_token_register(
        self, token_register: str
    ) -> Optional[AdminUserEntity]:
        """Find admin user by token register."""
        _LOGGER.info(f"Finding admin user by token register: [{token_register}]")

        stmt: Select[Tuple[AdminUserModel]] = select(AdminUserModel).where(
            AdminUserModel.token_register == token_register,
            AdminUserModel.is_active == True,
        )

        result: Result[Tuple[AdminUserModel]] = self._session.execute(stmt)
        user_model: AdminUserModel | None = result.scalar_one_or_none()

        if not user_model:
            _LOGGER.info(
                f"Admin user with token register [{token_register}] not found or not active"
            )
            return None

        return self._to_domain_entity(model=user_model)

    def _to_domain_entity(
        self, model: AdminUserModel
    ) -> AdminUserEntity:
        _LOGGER.info(f"Converting AdminUserModel to AdminUserEntity: [{model.id}]")
        return AdminUserEntity(
            email=model.email,
            name=model.name,
            last_name=model.last_name,
            phone=model.phone,
            rol=model.rol,
            identification=model.identification,
            id=model.id,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
            token_register=model.token_register,
        )

    def _to_database_model(
        self, entity: AdminUserEntity
    ) -> AdminUserModel:
        """
        Convert admin user entity to database model.
        """
        return AdminUserModel(
            id=entity.id,
            email=entity.email,
            password=entity.password,
            name=entity.name,
            last_name=entity.last_name,
            phone=entity.phone,
            rol=entity.rol,
            identification=entity.identification,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            deleted_at=entity.deleted_at,
            token_register=entity.token_register,
        )
