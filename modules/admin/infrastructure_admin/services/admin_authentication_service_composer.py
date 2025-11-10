from fastapi import Depends
from sqlalchemy.orm import Session

from common.config.common.settings import settings
from common.infrastructure.database.session import session_manager

from modules.admin.application_admin.services.admin_authentication_service import AdminAuthenticationService
from modules.admin.application_admin.use_cases.authenticate_admin_user import AuthenticateAdminUserUseCase
from modules.admin.application_admin.use_cases.login_admin_use_case import LoginAdminUseCase
from modules.admin.application_admin.use_cases.register_admin_use_case import RegisterAdminUseCase
from modules.admin.application_admin.use_cases.get_admin_survey_list_use_case import GetAdminSurveyListUseCase
from modules.admin.application_admin.use_cases.get_admin_survey_detail_use_case import GetAdminSurveyDetailUseCase # New import
from modules.admin.application_admin.use_cases.get_extensionist_list_use_case import GetExtensionistListUseCase
from modules.admin.infrastructure_admin.repositories.admin_authentication_repository import (
    AdminAuthenticationRepository,
)
from modules.admin.infrastructure_admin.repositories.extensionist_user_repository import (
    ExtensionistUserRepository,
)
from modules.surveys.domain_surveys.repositories.list_surveys_repository import (
    ListSurveysRepository,
)
from modules.surveys.infrastructure_surveys.repositories.postgresql.list_surveys_repository import PostgreSQLListSurveysRepository
from modules.surveys.application_surveys.services.get_survey_detail_service import GetSurveyDetailService # New import
from modules.surveys.infrastructure_surveys.services.get_survey_detail_service_composer import get_survey_detail_service # New import


def get_admin_authentication_service(
    session: Session = Depends(session_manager.get_session),
) -> AdminAuthenticationService:
    """
    Compose and return a configured admin authentication service.
    """
    admin_auth_repository = AdminAuthenticationRepository(session=session)

    return AdminAuthenticationService(
        admin_authentication_repository=admin_auth_repository,
        secret_key=settings.secret_api_key,
    )

def get_authenticate_admin_user_use_case(
    session: Session = Depends(session_manager.get_session),
) -> AuthenticateAdminUserUseCase:
    """
    Compose and return a configured authenticate admin user use case.
    """
    admin_auth_repository = AdminAuthenticationRepository(session=session)

    return AuthenticateAdminUserUseCase(
        admin_authentication_repository=admin_auth_repository,
        secret_key=settings.secret_api_key,
    )

def get_login_admin_use_case(
    session: Session = Depends(session_manager.get_session),
) -> LoginAdminUseCase:
    """
    Compose and return a configured login admin use case.
    """
    admin_auth_repository = AdminAuthenticationRepository(session=session)

    return LoginAdminUseCase(
        admin_authentication_repository=admin_auth_repository,
        secret_key=settings.secret_api_key,
    )

def get_register_admin_use_case(
    session: Session = Depends(session_manager.get_session),
) -> RegisterAdminUseCase:
    """
    Compose and return a configured register admin use case.
    """
    admin_auth_repository = AdminAuthenticationRepository(session=session)

    return RegisterAdminUseCase(
        admin_authentication_repository=admin_auth_repository,
        token_register_env=settings.admin_register_token,
    )

def get_admin_survey_list_use_case(
    session: Session = Depends(session_manager.get_session),
) -> GetAdminSurveyListUseCase:
    """
    Compose and return a configured GetAdminSurveyListUseCase.
    """
    list_surveys_repository: ListSurveysRepository = PostgreSQLListSurveysRepository(session=session)

    return GetAdminSurveyListUseCase(
        survey_repository=list_surveys_repository,
    )

def get_admin_survey_detail_use_case(
    get_survey_detail_service: GetSurveyDetailService = Depends(get_survey_detail_service),
) -> GetAdminSurveyDetailUseCase:
    """
    Compose and return a configured GetAdminSurveyDetailUseCase.
    """
    return GetAdminSurveyDetailUseCase(
        get_survey_detail_service=get_survey_detail_service,
    )


def get_get_extensionist_list_use_case(
    session: Session = Depends(session_manager.get_session),
) -> GetExtensionistListUseCase:
    """
    Compose and return a configured GetExtensionistListUseCase.
    """
    extensionist_user_repository = ExtensionistUserRepository(session=session)

    return GetExtensionistListUseCase(
        extensionist_user_repository=extensionist_user_repository,
    )
