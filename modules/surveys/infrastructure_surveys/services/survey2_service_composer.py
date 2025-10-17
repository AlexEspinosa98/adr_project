from sqlalchemy.orm import Session
from fastapi import Depends
from modules.surveys.application_surveys.services.survey2_service import Survey2Service
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey2_repository import PostgreSQLSurvey2Repository
from modules.surveys.infrastructure_surveys.repositories.postgresql.user_producter_repository import PostgreSQLUserProducterRepository
from modules.auth.infraestructure_auth.repositories.postgresql.auth_repository import PostgreSQLAuthRepository
from common.infrastructure.database.session import session_manager

def get_survey2_service(
    session: Session = Depends(session_manager.get_session)
) -> Survey2Service:
    survey_repository = PostgreSQLSurvey2Repository(session)
    auth_repository = PostgreSQLAuthRepository(session)
    user_producter_repository = PostgreSQLUserProducterRepository(session)
    return Survey2Service(survey_repository, auth_repository, user_producter_repository)
