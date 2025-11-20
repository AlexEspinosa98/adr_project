from abc import ABC, abstractmethod
from typing import Optional
from modules.surveys.domain_surveys.entities.survey_rejection_entity import SurveyRejection

class SurveyRejectionRepository(ABC):
    @abstractmethod
    def save(self, survey_rejection: SurveyRejection) -> SurveyRejection:
        pass

    @abstractmethod
    def get_by_survey_id_and_type(self, survey_id: int, survey_type: int) -> Optional[SurveyRejection]:
        pass