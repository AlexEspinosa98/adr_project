from logging import Logger

from fastapi import APIRouter,UploadFile, File, Depends, HTTPException, status as response_status
from modules.auth.infraestructure_auth.dtos.input_dto.user_extensionist import UserExtensionistInputDTO
from modules.auth.infraestructure_auth.dtos.input_dto.update_user_extensionist import UpdateUserExtensionistBodyDTO
from modules.auth.application_auth.dtos.input_dto.register_user_extensionist import RegisterUserExtensionistInputDTO
from modules.auth.application_auth.dtos.output_dto.register_user_extensionist import RegisterUserExtensionistOutputDTO
from modules.auth.application_auth.dtos.input_dto.update_user_extensionist import UpdateUserExtensionistInputDTO
from modules.auth.application_auth.dtos.output_dto.update_user_extensionist import UpdateUserExtensionistOutputDTO
from modules.auth.application_auth.services.auth_service import AuthService
from modules.auth.application_auth.mappers.auth_mapper import AuthMapper
from modules.auth.infraestructure_auth.services.auth_service_composer import get_auth_service
from common.infrastructure.api.dtos.response_dto import ApiResponseDTO
from common.infrastructure.logging.config import get_logger
from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.infraestructure_auth.api.dependencies.auth import get_current_user_from_token

_LOGGER: Logger = get_logger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])

# A simple mapping for demonstration. In a real app, this might come from a config or another service.
TYPE_ID_MAPPING = {
    "cc": 1,
    "ti": 2,
    "ce": 3,
}

@router.post("/register_extensionist", status_code=response_status.HTTP_201_CREATED)
def register_extensionist(
    input_dto: UserExtensionistInputDTO,
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponseDTO[RegisterUserExtensionistOutputDTO]:
    _LOGGER.info(f"Registering new extensionist with email {input_dto.email}")
    
    type_id_int = TYPE_ID_MAPPING.get(input_dto.type_id.lower())
    if type_id_int is None:
        raise HTTPException(status_code=400, detail=f"Invalid type_id: {input_dto.type_id}")

    app_input_dto = RegisterUserExtensionistInputDTO(
        name=input_dto.name,
        email=input_dto.email,
        phone=input_dto.phone,
        type_id=type_id_int,
        identification=input_dto.identification,
        city=input_dto.city,
        zone=input_dto.zone
    )
    
    try:
        result = auth_service.register_extensionist(app_input_dto)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
    return ApiResponseDTO.success_response(
        data=result,
        message="Extensionist registered successfully"
    )

@router.post("/user/signing-image", status_code=response_status.HTTP_200_OK)
def upload_signing_image(
    file: UploadFile = File(...),
    current_user: UserExtensionist = Depends(get_current_user_from_token),
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponseDTO[str]:
    _LOGGER.info(f"Uploading signing image for user {current_user.email}")
    
    try:
        contents = file.file.read()
        image_path = auth_service.upload_signing_image(
            user_id=current_user.id,
            image_data=contents,
            image_content_type=file.content_type
        )
    except Exception as e:
        _LOGGER.error(f"Error uploading image: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error uploading image.")
    finally:
        file.file.close()

    return ApiResponseDTO.success_response(
        data=image_path,
        message="Image uploaded successfully"
    )

@router.put("/extensionist", status_code=response_status.HTTP_200_OK)
def update_extensionist(
    input_dto: UpdateUserExtensionistBodyDTO,
    current_user: UserExtensionist = Depends(get_current_user_from_token),
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponseDTO[UpdateUserExtensionistOutputDTO]:
    _LOGGER.info(f"Updating extensionist {current_user.email}")
    
    app_input_dto = UpdateUserExtensionistInputDTO(
        user_id=current_user.id,
        **input_dto.model_dump(exclude_unset=True)
    )
    
    try:
        result = auth_service.update_extensionist(app_input_dto)
        output_dto = AuthMapper.to_update_user_extensionist_dto(result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    return ApiResponseDTO.success_response(
        data=output_dto,
        message="Extensionist updated successfully"
    )
