from sqlalchemy.orm import Session
from fastapi import Depends
from modules.surveys.application_surveys.services.get_survey_detail_service import GetSurveyDetailService
from modules.surveys.application_surveys.use_cases.get_survey_detail_use_case import GetSurveyDetailUseCase
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey_detail_repository import PostgreSQLSurveyDetailRepository
from common.infrastructure.database.session import session_manager

def get_survey_detail_service(
    session: Session = Depends(session_manager.get_session)
) -> GetSurveyDetailService:
    survey_detail_repository = PostgreSQLSurveyDetailRepository(session)
    get_survey_detail_use_case = GetSurveyDetailUseCase(survey_detail_repository)
    return GetSurveyDetailService(get_survey_detail_use_case)
