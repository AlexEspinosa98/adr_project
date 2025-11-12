from abc import ABC, abstractmethod
from typing import List, Optional

from modules.admin.application_admin.dtos.output_dto.admin_survey_list_output_dto import (
    AdminSurveyListOutputDTO,
)
from modules.admin.application_admin.dtos.output_dto.product_property_output_dto import ProductPropertyOutputDTO
from modules.admin.application_admin.dtos.output_dto.property_survey_output_dto import PropertySurveyOutputDTO


class AdminSurveyRepository(ABC):
    @abstractmethod
    def find_admin_surveys_with_filters(
        self,
        city: Optional[str] = None,
        extensionist_identification: Optional[str] = None,
        extensionist_name: Optional[str] = None,
    ) -> List[AdminSurveyListOutputDTO]:
        """
        Finds surveys for admin with optional filters including city, extensionist identification, and name.
        """

    @abstractmethod
    def find_product_properties_by_extensionist_id(
        self, extensionist_id: int, property_name: Optional[str] = None
    ) -> List[ProductPropertyOutputDTO]:
        """
        Finds unique product properties associated with a given extensionist ID.
        """

    @abstractmethod
    def find_surveys_by_property_id(
        self, property_id: int
    ) -> List[PropertySurveyOutputDTO]:
        """
        Finds all surveys (1, 2, and 3) associated with a property ID.
        """
