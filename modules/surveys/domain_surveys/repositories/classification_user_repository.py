from abc import ABC, abstractmethod
from typing import Optional
from modules.surveys.domain_surveys.entities.classification_user_entity import ClassificationUser

class ClassificationUserRepository(ABC):
    @abstractmethod
    def save(self, classification_user: ClassificationUser) -> ClassificationUser:
        pass

    @abstractmethod
    def find_by_survey_id(self, survey_id: int, survey_type: int) -> Optional[ClassificationUser]:
        pass
