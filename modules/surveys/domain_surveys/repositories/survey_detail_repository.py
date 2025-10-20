from abc import ABC, abstractmethod
from typing import Optional, Union
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3

class SurveyDetailRepository(ABC):
    @abstractmethod
    def get_survey_by_id_and_type(self, survey_id: int, survey_type: int) -> Optional[Union[Survey1, Survey2, Survey3]]:
        pass
