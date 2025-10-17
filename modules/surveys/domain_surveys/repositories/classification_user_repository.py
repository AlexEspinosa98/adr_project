from abc import ABC, abstractmethod
from typing import Optional
from modules.surveys.domain_surveys.entities.classification_user_entity import ClassificationUser

class ClassificationUserRepository(ABC):
    @abstractmethod
    def save(self, classification_user: ClassificationUser) -> ClassificationUser:
        pass
