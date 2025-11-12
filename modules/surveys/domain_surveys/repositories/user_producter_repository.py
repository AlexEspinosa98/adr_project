from abc import ABC, abstractmethod
from typing import Optional
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter


class UserProducterRepository(ABC):
    @abstractmethod
    def get_by_identification(self, identification: str) -> Optional[UserProducter]:
        pass

    @abstractmethod
    def save(self, producter: UserProducter) -> UserProducter:
        pass
