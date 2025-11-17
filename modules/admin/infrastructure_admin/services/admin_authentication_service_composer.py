from fastapi import Depends
from sqlalchemy.orm import Session

from common.config.common.settings import settings
from common.infrastructure.database.session import session_manager

from modules.admin.application_admin.services.admin_authentication_service import (
    AdminAuthenticationService,
)
from modules.admin.application_admin.use_cases.authenticate_admin_user import (
    AuthenticateAdminUserUseCase,
)
from modules.admin.application_admin.use_cases.login_admin_use_case import (
    LoginAdminUseCase,
)
from modules.admin.application_admin.use_cases.register_admin_use_case import (
    RegisterAdminUseCase,
)
from modules.admin.application_admin.use_cases.get_admin_survey_list_use_case import (
    GetAdminSurveyListUseCase,
)
from modules.admin.application_admin.use_cases.get_admin_survey_detail_use_case import (
    GetAdminSurveyDetailUseCase,
)
from modules.admin.application_admin.use_cases.get_extensionist_list_use_case import (
    GetExtensionistListUseCase,
)
from modules.admin.application_admin.use_cases.get_extensionist_name_id_phone_list_use_case import (
    GetExtensionistNameIdPhoneListUseCase,
)
from modules.admin.application_admin.use_cases.get_product_properties_by_extensionist_use_case import (
    GetProductPropertiesByExtensionistUseCase,
)
from modules.admin.application_admin.use_cases.get_surveys_by_property_id_use_case import (
    GetSurveysByPropertyIdUseCase,
)
from modules.admin.infrastructure_admin.repositories.admin_authentication_repository import (
    AdminAuthenticationRepository,
)
from modules.admin.infrastructure_admin.repositories.extensionist_user_repository import (
    ExtensionistUserRepository,
)
from modules.admin.domain_admin.repositories.admin_survey_repository import (
    AdminSurveyRepository,
)
from modules.admin.infrastructure_admin.repositories.admin_survey_repository import (
    PostgreSQLAdminSurveyRepository,
)
from modules.surveys.application_surveys.services.get_survey_detail_service import (
    GetSurveyDetailService,
)
from modules.surveys.infrastructure_surveys.services.get_survey_detail_service_composer import (
    get_survey_detail_service,
)
from modules.surveys.domain_surveys.repositories.classification_user_repository import (
    ClassificationUserRepository,
)
from modules.surveys.infrastructure_surveys.repositories.postgresql.classification_user_repository import (
    PostgreSQLClassificationUserRepository,
)

# Imports for AdminUpdateSurveyUseCase
from modules.admin.application_admin.use_cases.admin_update_survey_use_case import (
    AdminUpdateSurveyUseCase,
)
from modules.admin.application_admin.use_cases.log_admin_action import LogAdminAction
from modules.surveys.application_surveys.services.update_survey_service import (
    UpdateSurveyService,
)
from modules.surveys.infrastructure_surveys.services.update_survey_service_composer import (
    get_update_survey_service,
)


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
    admin_survey_repository: AdminSurveyRepository = PostgreSQLAdminSurveyRepository(
        session=session
    )

    return GetAdminSurveyListUseCase(
        admin_survey_repository=admin_survey_repository,
    )


def get_classification_user_repository(
    session: Session = Depends(session_manager.get_session),
) -> ClassificationUserRepository:
    return PostgreSQLClassificationUserRepository(session)


def get_admin_survey_detail_use_case(
    get_survey_detail_service: GetSurveyDetailService = Depends(
        get_survey_detail_service
    ),
    classification_user_repository: ClassificationUserRepository = Depends(
        get_classification_user_repository
    ),
) -> GetAdminSurveyDetailUseCase:
    """
    Compose and return a configured GetAdminSurveyDetailUseCase.
    """
    return GetAdminSurveyDetailUseCase(
        get_survey_detail_service=get_survey_detail_service,
        classification_user_repository=classification_user_repository,
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


def get_get_extensionist_name_id_phone_list_use_case(
    session: Session = Depends(session_manager.get_session),
) -> GetExtensionistNameIdPhoneListUseCase:
    """
    Compose and return a configured GetExtensionistNameIdPhoneListUseCase.
    """
    extensionist_user_repository = ExtensionistUserRepository(session=session)

    return GetExtensionistNameIdPhoneListUseCase(
        extensionist_user_repository=extensionist_user_repository,
    )


def get_product_properties_by_extensionist_use_case(
    session: Session = Depends(session_manager.get_session),
) -> GetProductPropertiesByExtensionistUseCase:
    """
    Compose and return a configured GetProductPropertiesByExtensionistUseCase.
    """
    admin_survey_repository: AdminSurveyRepository = PostgreSQLAdminSurveyRepository(
        session=session
    )

    return GetProductPropertiesByExtensionistUseCase(
        admin_survey_repository=admin_survey_repository,
    )


def get_surveys_by_property_id_use_case(
    session: Session = Depends(session_manager.get_session),
) -> GetSurveysByPropertyIdUseCase:
    """
    Compose and return a configured GetSurveysByPropertyIdUseCase.
    """
    admin_survey_repository: AdminSurveyRepository = PostgreSQLAdminSurveyRepository(
        session=session
    )
    return GetSurveysByPropertyIdUseCase(
        admin_survey_repository=admin_survey_repository
    )


def get_admin_update_survey_use_case(
    session: Session = Depends(session_manager.get_session),
    update_survey_service: UpdateSurveyService = Depends(get_update_survey_service),
) -> AdminUpdateSurveyUseCase:
    """
    Compose and return a configured AdminUpdateSurveyUseCase.
    """
    log_admin_action = LogAdminAction(db_session=session)
    return AdminUpdateSurveyUseCase(
        update_survey_service=update_survey_service,
        log_admin_action=log_admin_action,
    )