from typing import Optional, Tuple
from datetime import datetime
from modules.surveys.domain_surveys.repositories.list_surveys_repository import ListSurveysRepository
from modules.surveys.application_surveys.dtos.output_dto.survey_list_item_dto import SurveyListItemDTO
from common.application.dtos.input_dto.pagination_dto import PaginationInputDTO
from common.application.dtos.output_dto.pagination_dto import PaginatedOutputDTO

class ListSurveysUseCase:
    def __init__(self, list_surveys_repository: ListSurveysRepository):
        self._list_surveys_repository = list_surveys_repository

    def execute(
        self,
        pagination: PaginationInputDTO,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        farm_name: Optional[str] = None,
        survey_type: Optional[int] = None,
    ) -> PaginatedOutputDTO[SurveyListItemDTO]:
        
        surveys, total_items = self._list_surveys_repository.list_surveys(
            pagination=pagination,
            start_date=start_date,
            end_date=end_date,
            farm_name=farm_name,
            survey_type=survey_type
        )

        return PaginatedOutputDTO.create_response(
            items=surveys,
            pagination_input=pagination,
            total_items=total_items
        )
