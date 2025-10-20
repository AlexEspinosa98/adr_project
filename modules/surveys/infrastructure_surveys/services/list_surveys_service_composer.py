from sqlalchemy.orm import Session
from fastapi import Depends
from modules.surveys.application_surveys.services.list_surveys_service import ListSurveysService
from modules.surveys.application_surveys.use_cases.list_surveys_use_case import ListSurveysUseCase
from modules.surveys.infrastructure_surveys.repositories.postgresql.list_surveys_repository import PostgreSQLListSurveysRepository
from common.infrastructure.database.session import session_manager

def get_list_surveys_service(
    session: Session = Depends(session_manager.get_session)
) -> ListSurveysService:
    list_surveys_repository = PostgreSQLListSurveysRepository(session)
    list_surveys_use_case = ListSurveysUseCase(list_surveys_repository)
    return ListSurveysService(list_surveys_use_case)
