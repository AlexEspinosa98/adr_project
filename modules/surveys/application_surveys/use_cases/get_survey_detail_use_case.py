from typing import Optional
from modules.surveys.domain_surveys.repositories.survey_detail_repository import SurveyDetailRepository
from modules.surveys.application_surveys.dtos.output_dto.survey_detail_output_dto import SurveyDetailOutputDTO
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3

class GetSurveyDetailUseCase:
    def __init__(self, survey_detail_repository: SurveyDetailRepository):
        self._survey_detail_repository = survey_detail_repository

    def execute(self, survey_id: int, survey_type: int) -> Optional[SurveyDetailOutputDTO]:
        survey_entity = self._survey_detail_repository.get_survey_by_id_and_type(survey_id, survey_type)

        if not survey_entity:
            return None
        
        # Map the entity to the SurveyDetailOutputDTO
        # This mapping needs to handle the different fields across survey types
        # and exclude classification_user.
        
        survey_dict = survey_entity.dict()
        survey_dict.pop('classification_user', None) # Remove classification_user if present

        # Handle producter_id vs user_producter_id
        if isinstance(survey_entity, Survey2):
            survey_dict['user_producter_id'] = survey_dict.pop('producter_id', None)
        
        return SurveyDetailOutputDTO(**survey_dict)
