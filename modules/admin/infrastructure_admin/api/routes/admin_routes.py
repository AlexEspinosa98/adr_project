from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from common.infrastructure.api import decorators as common_decorators
from common.infrastructure.api.dtos.response_dto import ApiResponseDTO

from modules.admin.application_admin.dtos.input_dto.admin_login_dto import AdminLoginInputDTO
from modules.admin.application_admin.dtos.input_dto.admin_register_dto import AdminRegisterInputDTO
from modules.admin.application_admin.dtos.output_dto.admin_login_output_dto import AdminLoginOutputDTO
from modules.admin.application_admin.dtos.output_dto.admin_user_dto import AdminUserDTO
from modules.admin.application_admin.services.admin_authentication_service import AdminAuthenticationService
from modules.admin.application_admin.use_cases.login_admin_use_case import LoginAdminUseCase
from modules.admin.application_admin.use_cases.register_admin_use_case import RegisterAdminUseCase
from modules.admin.infrastructure_admin.services.admin_authentication_service_composer import (
    get_admin_authentication_service,
    get_login_admin_use_case,
    get_register_admin_use_case,
)


router = APIRouter()


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
        register_admin_use_case (RegisterAdminUseCase): The use case for admin registration.

    Returns:
        ApiResponseDTO[AdminUserDTO]: The API response containing the created admin user.
    """
    admin_user = await register_admin_use_case.execute(
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
