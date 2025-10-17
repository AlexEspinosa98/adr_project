from abc import ABC, abstractmethod
from typing import Optional

from modules.auth.domain_auth.entities.auth_entities import UserExtensionist, UserProducter
from common.infrastructure.database.models.auth import ProductProperty

class AuthRepository(ABC):
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

    @abstractmethod
    def get_user_by_api_key(self, api_key: str) -> Optional[UserExtensionist]:
        """Find a user by api_key."""
        pass

    @abstractmethod
    def save_producter(self, producter: UserProducter) -> UserProducter:
        """Save a producter."""
        pass

    @abstractmethod
    def get_property_by_name(self, name: str) -> Optional[ProductProperty]:
        """Get property by name."""
        pass

    @abstractmethod
    def save_property(self, property: ProductProperty) -> ProductProperty:
        """Save a property."""
        pass

    @abstractmethod
    def save_extensionist(self, extensionist: UserExtensionist) -> UserExtensionist:
        """Save an extensionist."""
        pass