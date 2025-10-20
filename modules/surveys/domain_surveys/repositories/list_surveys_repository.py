from abc import ABC, abstractmethod
from typing import Optional, Tuple
from datetime import datetime
from modules.surveys.application_surveys.dtos.output_dto.survey_list_item_dto import SurveyListItemDTO
from common.application.dtos.input_dto.pagination_dto import PaginationInputDTO

class ListSurveysRepository(ABC):
    @abstractmethod
    def list_surveys(
        self,
        pagination: PaginationInputDTO,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        farm_name: Optional[str] = None,
        survey_type: Optional[int] = None,
    ) -> Tuple[list[SurveyListItemDTO], int]:
        pass
