from abc import ABC, abstractmethod

from modules.admin.domain_admin.entities.admin_user_entity import (
    AdminUser as AdminUserEntity,
)
from common.domain import repositories as common_repositories


class AdminAuthenticationRepository(
    common_repositories.BaseRepository[AdminUserEntity], ABC
):
    """
    Repository interface for ADMIN AUTHENTICATION-specific operations.
    """

    @abstractmethod
    def find_active_admin_user_by_id(self, user_id: int) -> AdminUserEntity | None:
        """
        Find active admin user for authentication by ID.

        Returns None if user is not found or not active.
        """

    @abstractmethod
    def find_admin_user_by_email_and_password(
        self, email: str, password: str
    ) -> AdminUserEntity | None:
        """Find admin user by email and password for authentication."""

    @abstractmethod
    def find_admin_user_by_email(self, email: str) -> AdminUserEntity | None:
        """Find admin user by email."""

    @abstractmethod
    def find_admin_user_by_token_register(
        self, token_register: str
    ) -> AdminUserEntity | None:
        """Find admin user by token register."""
