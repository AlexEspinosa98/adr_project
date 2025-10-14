from abc import ABC, abstractmethod
from typing import Optional

from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from common.domain.repositories.base_repository import BaseRepository

class AuthRepository(BaseRepository[UserExtensionist], ABC):
    """
    Repository interface for Auth-specific operations.
    """

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserExtensionist]:
        """Find a user by email."""
        pass

    @abstractmethod
    def get_user_by_identification(self, identification: str) -> Optional[UserExtensionist]:
        """Find a user by identification."""
        pass

    @abstractmethod
    def get_user_by_token(self, token: str) -> Optional[UserExtensionist]:
        """Find a user by token."""
        pass
