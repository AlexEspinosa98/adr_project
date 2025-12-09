from abc import ABC, abstractmethod
from typing import List, Optional

from common.domain.repositories import BaseRepository
from modules.admin.domain_admin.entities.extensionist_user_entity import (
    ExtensionistUser,
)


class ExtensionistUserRepository(BaseRepository[ExtensionistUser], ABC):
    @abstractmethod
    def find_all_with_filters(
        self,
        name: Optional[str] = None,
        identification: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        city: Optional[str] = None,
    ) -> List[ExtensionistUser]:
        """Find all extensionist users with optional filters."""
