from sqlalchemy.orm import Session
from fastapi import Depends
from modules.surveys.application_surveys.services.survey3_service import Survey3Service
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey3_repository import PostgreSQLSurvey3Repository
from modules.surveys.infrastructure_surveys.repositories.postgresql.user_producter_repository import PostgreSQLUserProducterRepository
from modules.surveys.infrastructure_surveys.repositories.postgresql.product_property_repository import PostgreSQLProductPropertyRepository
from modules.auth.infraestructure_auth.repositories.postgresql.auth_repository import PostgreSQLAuthRepository
from common.infrastructure.database.session import session_manager

def get_survey3_service(
    session: Session = Depends(session_manager.get_session)
) -> Survey3Service:
    survey_repository = PostgreSQLSurvey3Repository(session)
    auth_repository = PostgreSQLAuthRepository(session)
    user_producter_repository = PostgreSQLUserProducterRepository(session)
    product_property_repository = PostgreSQLProductPropertyRepository(session)
    return Survey3Service(survey_repository, auth_repository, user_producter_repository, product_property_repository)
