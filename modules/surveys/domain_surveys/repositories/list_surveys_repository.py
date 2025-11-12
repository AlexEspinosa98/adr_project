from abc import ABC, abstractmethod
from typing import Optional, Tuple, List
from datetime import datetime
from modules.surveys.application_surveys.dtos.output_dto.survey_list_item_dto import (
    SurveyListItemDTO,
)
from common.application.dtos.input_dto.pagination_dto import PaginationInputDTO
from modules.surveys.domain_surveys.entities.survey_entity import (
    Survey,
)  # Import the new combined Survey entity


class ListSurveysRepository(ABC):
    @abstractmethod
    def list_surveys(
        self,
        pagination: PaginationInputDTO,
        api_key: Optional[str],
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        farm_name: Optional[str] = None,
        survey_type: Optional[int] = None,
    ) -> Tuple[list[SurveyListItemDTO], int]:
        pass

    @abstractmethod
    def find_admin_surveys_with_filters(
        self, city: Optional[str] = None, extensionist: Optional[str] = None
    ) -> List[Survey]:
        pass
