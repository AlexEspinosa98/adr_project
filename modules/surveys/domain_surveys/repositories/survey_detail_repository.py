from abc import ABC, abstractmethod
from typing import Optional, Union
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3
from modules.surveys.domain_surveys.repositories.user_producter_repository import UserProducterRepository # New import
from modules.surveys.domain_surveys.repositories.product_property_repository import ProductPropertyRepository # New import

class SurveyDetailRepository(ABC):
    def __init__(
        self,
        user_producter_repository: UserProducterRepository,
        product_property_repository: ProductPropertyRepository,
    ):
        self._user_producter_repository = user_producter_repository
        self._product_property_repository = product_property_repository

    @abstractmethod
    def get_survey_by_id_and_type(self, survey_id: int, survey_type: int) -> Optional[Union[Survey1, Survey2, Survey3]]:
        pass

    @abstractmethod
    def get_classification_user_by_survey_id(self, survey_id: int, survey_type: int) -> Optional[dict]:
        pass
