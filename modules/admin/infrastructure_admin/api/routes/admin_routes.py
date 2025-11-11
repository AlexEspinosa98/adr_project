from typing import List, Optional, Union # Modified import

from fastapi import APIRouter, Depends, status, HTTPException # Added HTTPException
from fastapi.responses import JSONResponse

from common.infrastructure.api import decorators as common_decorators
from common.infrastructure.api.dtos.response_dto import ApiResponseDTO

from modules.admin.application_admin.dtos.input_dto.admin_login_dto import AdminLoginInputDTO
from modules.admin.application_admin.dtos.input_dto.admin_register_dto import AdminRegisterInputDTO
from modules.admin.application_admin.dtos.input_dto.admin_survey_filter_input_dto import AdminSurveyFilterInputDTO
from modules.admin.application_admin.dtos.output_dto.admin_login_output_dto import AdminLoginOutputDTO
from modules.admin.application_admin.dtos.output_dto.admin_user_dto import AdminUserDTO
from modules.admin.application_admin.dtos.output_dto.admin_survey_output_dto import AdminSurveyOutputDTO
from modules.admin.application_admin.dtos.output_dto.admin_survey_list_output_dto import AdminSurveyListOutputDTO
from modules.admin.application_admin.dtos.output_dto.admin_survey1_detail_output_dto import AdminSurvey1DetailOutputDTO # New import
from modules.admin.application_admin.dtos.output_dto.admin_survey2_detail_output_dto import AdminSurvey2DetailOutputDTO # New import
from modules.admin.application_admin.dtos.output_dto.admin_survey3_detail_output_dto import AdminSurvey3DetailOutputDTO
from modules.admin.application_admin.dtos.output_dto.extensionist_output_dto import ExtensionistOutputDTO
from modules.admin.application_admin.dtos.output_dto.extensionist_name_id_phone_output_dto import ExtensionistNameIdPhoneOutputDTO
from modules.admin.application_admin.dtos.output_dto.product_property_output_dto import ProductPropertyOutputDTO
from modules.admin.application_admin.services.admin_authentication_service import AdminAuthenticationService
from modules.admin.application_admin.use_cases.login_admin_use_case import LoginAdminUseCase
from modules.admin.application_admin.use_cases.register_admin_use_case import RegisterAdminUseCase
from modules.admin.application_admin.use_cases.get_admin_survey_list_use_case import GetAdminSurveyListUseCase
from modules.admin.application_admin.use_cases.get_admin_survey_detail_use_case import GetAdminSurveyDetailUseCase
from modules.admin.application_admin.use_cases.get_extensionist_list_use_case import GetExtensionistListUseCase
from modules.admin.application_admin.use_cases.get_extensionist_name_id_phone_list_use_case import GetExtensionistNameIdPhoneListUseCase
from modules.admin.application_admin.use_cases.get_product_properties_by_extensionist_use_case import GetProductPropertiesByExtensionistUseCase
from modules.admin.infrastructure_admin.services.admin_authentication_service_composer import (
    get_admin_authentication_service,
    get_login_admin_use_case,
    get_register_admin_use_case,
    get_admin_survey_list_use_case,
    get_admin_survey_detail_use_case,
    get_get_extensionist_list_use_case,
    get_get_extensionist_name_id_phone_list_use_case,
    get_product_properties_by_extensionist_use_case,
)

from fastapi import Depends, status, HTTPException
from common.infrastructure.api.dtos.response_dto import ApiResponseDTO
from common.infrastructure.authentication.user_authorizer import get_current_user
from common.application.dtos.output_dto.authentication_dto import AuthenticatedUserDTO
from common.infrastructure.database.session import session_manager
from sqlalchemy.orm import Session
from modules.surveys.application_surveys.use_cases.update_survey_state import UpdateSurveyState
from modules.surveys.application_surveys.dtos.input_dto.update_survey_state_input_dto import UpdateSurveyStateInputDTO
# Removed old imports for Survey1DetailOutputDTO, Survey2DetailOutputDTO, Survey3DetailOutputDTO
#logger setup
from common.infrastructure.logging.config import get_logger
_LOGGER = get_logger(__name__)

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post(
    "/login",
    response_model=ApiResponseDTO[AdminLoginOutputDTO],
    status_code=status.HTTP_200_OK,
    summary="Admin Login",
    description="Authenticates an admin user and returns an access token.",
    tags=["Admin Authentication"],
)
@common_decorators.handle_exceptions
@common_decorators.handle_authentication_exceptions
async def admin_login(
    login_data: AdminLoginInputDTO,
    login_admin_use_case: LoginAdminUseCase = Depends(get_login_admin_use_case),
) -> ApiResponseDTO[AdminLoginOutputDTO]:
    """
    Handles admin user login.

    Args:
        login_data (AdminLoginInputDTO): The login credentials.
        login_admin_use_case (LoginAdminUseCase): The use case for admin login.

    Returns:
        ApiResponseDTO[AdminLoginOutputDTO]: The API response containing the access token.
    """
    token = login_admin_use_case.execute(login_data.email, login_data.password)
    return ApiResponseDTO.success_response(
        data=AdminLoginOutputDTO(access_token=token.raw_token),
        message="Admin logged in successfully",
    )


@router.post(
    "/register",
    response_model=ApiResponseDTO[AdminUserDTO],
    status_code=status.HTTP_201_CREATED,
    summary="Admin Registration",
    description="Registers a new admin user.",
    tags=["Admin Authentication"],
)
@common_decorators.handle_exceptions
@common_decorators.handle_authentication_exceptions
async def admin_register(
    register_data: AdminRegisterInputDTO,
    register_admin_use_case: RegisterAdminUseCase = Depends(get_register_admin_use_case),
) -> ApiResponseDTO[AdminUserDTO]:
    """
    Handles admin user registration.

    Args:
        register_data (AdminRegisterInputDTO): The registration data.
        register_admin_use_case (RegisterAdminUseCase): The use case for admin registration.)

    Returns:
        ApiResponseDTO[AdminUserDTO]: The API response containing the created admin user.
    """
    admin_user = register_admin_use_case.execute(
        name=register_data.name,
        last_name=register_data.last_name,
        email=register_data.email,
        password=register_data.password,
        phone=register_data.phone,
        rol=register_data.rol,
        identification=register_data.identification,
        token_register=register_data.token_register,
    )
    return ApiResponseDTO.success_response(
        data=admin_user,
        message="Admin registered successfully",
    )


@router.get(
    "/extensionists",
    response_model=ApiResponseDTO[List[ExtensionistOutputDTO]],
    status_code=status.HTTP_200_OK,
    summary="Get Extensionist List",
    description="Retrieves a list of extensionist users with optional filters.",
    tags=["Admin Users"],
    # dependencies=[Depends(get_current_user)],
)
# @common_decorators.handle_exceptions
# @common_decorators.handle_authentication_exceptions
async def get_extensionist_list(
    name: Optional[str] = None,
    identification: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    get_extensionist_list_use_case: GetExtensionistListUseCase = Depends(
        get_get_extensionist_list_use_case
    ),
) -> ApiResponseDTO[List[ExtensionistOutputDTO]]:
    """
    Handles fetching a list of extensionist users with optional filters.
    """
    extensionists = get_extensionist_list_use_case.execute(
        name=name,
        identification=identification,
        email=email,
        phone=phone,
    )
    return ApiResponseDTO.success_response(
        data=extensionists,
        message="Extensionist list fetched successfully",
    )


@router.get(
    "/extensionists/names-ids-phones",
    response_model=ApiResponseDTO[List[ExtensionistNameIdPhoneOutputDTO]],
    status_code=status.HTTP_200_OK,
    summary="Get Extensionist Names, IDs, and Phones List",
    description="Retrieves a list of extensionist names, identification numbers, and phone numbers, with optional filters.",
    tags=["Admin Users"],
    # dependencies=[Depends(get_current_user)],
)
@common_decorators.handle_exceptions
@common_decorators.handle_authentication_exceptions
async def get_extensionist_name_id_phone_list(
    name: Optional[str] = None,
    identification: Optional[str] = None,
    phone: Optional[str] = None,
    get_extensionist_name_id_phone_list_use_case: GetExtensionistNameIdPhoneListUseCase = Depends(
        get_get_extensionist_name_id_phone_list_use_case
    ),
) -> ApiResponseDTO[List[ExtensionistNameIdPhoneOutputDTO]]:
    """
    Handles fetching a list of extensionist names, identification numbers, and phone numbers with optional filters.
    """
    extensionists = get_extensionist_name_id_phone_list_use_case.execute(
        name=name,
        identification=identification,
        phone=phone,
    )
    return ApiResponseDTO.success_response(
        data=extensionists,
        message="Extensionist names, identification, and phones list fetched successfully",
    )


@router.get(
    "/extensionists/{extensionist_id}/product-properties",
    response_model=ApiResponseDTO[List[ProductPropertyOutputDTO]],
    status_code=status.HTTP_200_OK,
    summary="Get Product Properties by Extensionist ID",
    description="Retrieves a list of unique product properties associated with a given extensionist ID, with optional filtering by property name.",
    tags=["Admin Surveys"],
)
@common_decorators.handle_exceptions
@common_decorators.handle_authentication_exceptions
async def get_product_properties_by_extensionist(
    extensionist_id: int,
    property_name: Optional[str] = None,
    get_product_properties_by_extensionist_use_case: GetProductPropertiesByExtensionistUseCase = Depends(get_product_properties_by_extensionist_use_case),
) -> ApiResponseDTO[List[ProductPropertyOutputDTO]]:
    """
    Handles fetching a list of unique product properties associated with a given extensionist ID.
    """
    product_properties = get_product_properties_by_extensionist_use_case.execute(extensionist_id, property_name)
    return ApiResponseDTO.success_response(
        data=product_properties,
        message=f"Product properties for extensionist ID {extensionist_id} fetched successfully",
    )


@router.get(
    "/surveys",
    response_model=ApiResponseDTO[List[AdminSurveyListOutputDTO]],
    status_code=status.HTTP_200_OK,
    summary="Get Admin Survey List",
    description="Retrieves a list of surveys for admin with optional filters.",
    tags=["Admin Surveys"],
)
# @common_decorators.handle_exceptions
# @common_decorators.handle_authentication_exceptions
async def get_admin_survey_list(
    city: Optional[str] = None,
    extensionist_identification: Optional[str] = None,
    extensionist_name: Optional[str] = None,
    get_admin_survey_list_use_case: GetAdminSurveyListUseCase = Depends(get_admin_survey_list_use_case),
) -> ApiResponseDTO[List[AdminSurveyListOutputDTO]]:
    """
    Handles fetching a list of surveys for admin with optional filters.

    Args:
        city (Optional[str]): Optional filter for city.
        extensionist_identification (Optional[str]): Optional filter for extensionist identification.
        extensionist_name (Optional[str]): Optional filter for extensionist name.
        get_admin_survey_list_use_case (GetAdminSurveyListUseCase): The use case for getting admin survey list.

    Returns:
        ApiResponseDTO[List[AdminSurveyListOutputDTO]]: The API response containing the list of surveys.
    """
    surveys = get_admin_survey_list_use_case.execute(
        city=city,
        extensionist_identification=extensionist_identification,
        extensionist_name=extensionist_name,
    )
    return ApiResponseDTO.success_response(
        data=surveys,
        message="Admin survey list fetched successfully",
    )


@router.get(
    "/surveys/{survey_type}/{survey_id}",
    response_model=ApiResponseDTO[Union[AdminSurvey1DetailOutputDTO, AdminSurvey2DetailOutputDTO, AdminSurvey3DetailOutputDTO]], # Changed response_model
    status_code=status.HTTP_200_OK,
    summary="Get Admin Survey Detail",
    description="Retrieves full details of a single survey for admin.",
    tags=["Admin Surveys"],
)
@common_decorators.handle_exceptions
@common_decorators.handle_authentication_exceptions
async def get_admin_survey_detail(
    survey_type: int,
    survey_id: int,
    get_admin_survey_detail_use_case: GetAdminSurveyDetailUseCase = Depends(get_admin_survey_detail_use_case),
) -> ApiResponseDTO[Union[AdminSurvey1DetailOutputDTO, AdminSurvey2DetailOutputDTO, AdminSurvey3DetailOutputDTO]]: # Changed return type
    """
    Handles fetching full details of a single survey for admin.

    Args:
        survey_type (int): The type of the survey (1, 2, or 3).
        survey_id (int): The ID of the survey.
        get_admin_survey_detail_use_case (GetAdminSurveyDetailUseCase): The use case for getting admin survey detail.

    Returns:
        ApiResponseDTO[Union[AdminSurvey1DetailOutputDTO, AdminSurvey2DetailOutputDTO, AdminSurvey3DetailOutputDTO]]: The API response containing the survey details.
    """
    survey_detail = get_admin_survey_detail_use_case.execute(survey_id, survey_type)

    if not survey_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Survey not found")

    return ApiResponseDTO.success_response(
        data=survey_detail,
        message=f"Survey type {survey_type} with ID {survey_id} retrieved successfully",
    )


@router.put(
    "/surveys/{survey_type}/{survey_id}/state",
    response_model=ApiResponseDTO[str],
    status_code=status.HTTP_200_OK,
    summary="Update Survey State",
    description="Updates the state of a specific survey (1, 2, or 3) to ACCEPTED or REJECTED.",
    tags=["Admin Surveys"],
)
# @common_decorators.handle_exceptions
# @common_decorators.handle_authentication_exceptions
async def update_survey_state(
    survey_type: int,
    survey_id: int,
    state_update: UpdateSurveyStateInputDTO,
    current_user: AuthenticatedUserDTO = Depends(get_current_user),
    db_session: Session = Depends(session_manager.get_session),
) -> ApiResponseDTO[str]:
    _LOGGER.info(f"Admin user {current_user.user_id} updating state for survey type {survey_type} with ID {survey_id} to {state_update.new_state}")

    try:
        update_survey_state_use_case = UpdateSurveyState(db_session)
        updated_survey = update_survey_state_use_case.execute(
            survey_type=survey_type,
            survey_id=survey_id,
            new_state=state_update.new_state,
            admin_user_id=current_user.user_id,
        )
        return ApiResponseDTO.success_response(
            data=f"Survey {survey_type} with ID {survey_id} state updated to {updated_survey.state}",
            message="Survey state updated successfully",
        )
    except ValueError as e:
        _LOGGER.error(f"Error updating survey state: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        _LOGGER.error(f"Unexpected error updating survey state: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred.")

