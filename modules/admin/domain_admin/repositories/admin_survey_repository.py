from abc import ABC, abstractmethod
from typing import List, Optional

from modules.admin.application_admin.dtos.output_dto.admin_survey_list_output_dto import (
    AdminSurveyListOutputDTO,
)


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
