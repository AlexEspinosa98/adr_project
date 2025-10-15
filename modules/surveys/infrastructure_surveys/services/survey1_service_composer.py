from sqlalchemy.orm import Session
from fastapi import Depends
from modules.surveys.application_surveys.services.survey1_service import Survey1Service
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey1_repository import PostgreSQLSurvey1Repository
from common.infrastructure.database.session import session_manager

def get_survey1_service(
    session: Session = Depends(session_manager.get_session)
) -> Survey1Service:
    repository = PostgreSQLSurvey1Repository(session)
    return Survey1Service(repository)
