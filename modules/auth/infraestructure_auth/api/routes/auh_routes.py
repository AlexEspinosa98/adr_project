"""
API routes for authentication module.
"""

from logging import Logger

from fastapi import APIRouter, Depends, status as response_status
from modules.auth.infraestructure_auth.dtos.input_dto.user_extensionist import UserExtensionistInputDTO
from common.infrastructure.api import dtos as common_infrastructure_dtos
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register_extensionist", status_code=response_status.HTTP_201_CREATED)
def register_extensionist(
    input_dto: UserExtensionistInputDTO
    auth_service=Depends(),  # Placeholder for actual service dependency
    ) -> common_infrastructure_dtos.ApiResponseDTO[dict[str, str]]:
    _LOGGER.info("Registering new extensionist")
    # Here you would typically call a service to handle the registration logic.

    return common_infrastructure_dtos.ApiResponseDTO[dict[str, str]](
        data={"message": "Extensionist registered successfully"}
    )