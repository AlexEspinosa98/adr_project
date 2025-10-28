from abc import ABC, abstractmethod
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2

class Survey2Repository(ABC):
    @abstractmethod
    def save(self, survey: Survey2) -> Survey2:
        pass

    @abstractmethod
    def get_by_id(self, survey_id: int) -> Survey2 | None:
        pass