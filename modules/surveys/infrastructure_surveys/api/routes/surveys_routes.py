from logging import Logger
from fastapi import APIRouter, Depends, HTTPException, status as response_status
from modules.surveys.application_surveys.dtos.input_dto.create_survey1 import CreateSurvey1InputDTO
from modules.surveys.application_surveys.dtos.output_dto.create_survey1 import CreateSurvey1OutputDTO
from modules.surveys.application_surveys.services.survey1_service import Survey1Service
from modules.surveys.infrastructure_surveys.services.survey1_service_composer import get_survey1_service
from common.infrastructure.api.dtos.response_dto import ApiResponseDTO
from common.infrastructure.logging.config import get_logger
from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.infraestructure_auth.api.dependencies.auth import get_current_user_from_token

_LOGGER: Logger = get_logger(__name__)

router = APIRouter(prefix="/surveys", tags=["surveys"])

@router.post("/1", status_code=response_status.HTTP_201_CREATED)
def create_survey1(
    input_dto: CreateSurvey1InputDTO,
    survey_service: Survey1Service = Depends(get_survey1_service),
    current_user: UserExtensionist = Depends(get_current_user_from_token),
) -> ApiResponseDTO[CreateSurvey1OutputDTO]:
    _LOGGER.info(f"Creating new survey 1 for user {current_user.email}")
    
    try:
        result = survey_service.create_survey1(input_dto)
    except Exception as e:
        _LOGGER.error(f"Error creating survey 1: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error creating survey 1.")
    
    return ApiResponseDTO.success_response(
        data=result,
        message="Survey 1 created successfully"
    )
