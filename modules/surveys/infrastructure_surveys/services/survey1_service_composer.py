from sqlalchemy.orm import Session
from fastapi import Depends
from modules.surveys.application_surveys.services.survey1_service import Survey1Service
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey1_repository import PostgreSQLSurvey1Repository
from modules.surveys.infrastructure_surveys.repositories.postgresql.user_producter_repository import PostgreSQLUserProducterRepository
from modules.surveys.infrastructure_surveys.repositories.postgresql.product_property_repository import PostgreSQLProductPropertyRepository
from modules.surveys.infrastructure_surveys.repositories.postgresql.classification_user_repository import PostgreSQLClassificationUserRepository
from modules.auth.infraestructure_auth.repositories.postgresql.auth_repository import PostgreSQLAuthRepository
from common.infrastructure.database.session import session_manager

def get_survey1_service(
    session: Session = Depends(session_manager.get_session)
) -> Survey1Service:
    survey_repository = PostgreSQLSurvey1Repository(session)
    auth_repository = PostgreSQLAuthRepository(session)
    user_producter_repository = PostgreSQLUserProducterRepository(session)
    product_property_repository = PostgreSQLProductPropertyRepository(session)
    classification_user_repository = PostgreSQLClassificationUserRepository(session)
    return Survey1Service(survey_repository, auth_repository, user_producter_repository, product_property_repository, classification_user_repository)