from abc import ABC, abstractmethod
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3

class Survey3Repository(ABC):
    @abstractmethod
    def save(self, survey: Survey3) -> Survey3:
        pass
