from abc import ABC, abstractmethod
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1

class Survey1Repository(ABC):
    @abstractmethod
    def save(self, survey: Survey1) -> Survey1:
        pass
