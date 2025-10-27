from typing import Optional
from datetime import datetime
from modules.surveys.application_surveys.use_cases.list_surveys_use_case import ListSurveysUseCase
from modules.surveys.application_surveys.dtos.output_dto.survey_list_item_dto import SurveyListItemDTO
from common.application.dtos.input_dto.pagination_dto import PaginationInputDTO
from common.application.dtos.output_dto.pagination_dto import PaginatedOutputDTO

class ListSurveysService:
    def __init__(self, list_surveys_use_case: ListSurveysUseCase):
        self._list_surveys_use_case = list_surveys_use_case

    def list_surveys(
        self,
        pagination: PaginationInputDTO,
        api_key: Optional[str],
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        farm_name: Optional[str] = None,
        survey_type: Optional[int] = None,
    ) -> PaginatedOutputDTO[SurveyListItemDTO]:
        
        return self._list_surveys_use_case.execute(
            pagination=pagination,
            api_key=api_key,
            start_date=start_date,
            end_date=end_date,
            farm_name=farm_name,
            survey_type=survey_type
        )
