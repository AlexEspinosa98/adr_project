from logging import Logger
from modules.auth.application_auth.dtos.input_dto.register_user_extensionist import RegisterUserExtensionistInputDTO
from modules.auth.application_auth.dtos.output_dto.register_user_extensionist import RegisterUserExtensionistOutputDTO
from modules.auth.application_auth.mappers.auth_mapper import AuthMapper
from modules.auth.application_auth.use_cases.register_user_extensionist import RegisterUserExtensionistUseCase
from modules.auth.application_auth.use_cases.upload_signing_image import UploadSigningImageUseCase
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class AuthService:
    def __init__(self, auth_repository: AuthRepository):
        self.logger = _LOGGER
        self.auth_repository = auth_repository

    def register_extensionist(self, data: RegisterUserExtensionistInputDTO) -> RegisterUserExtensionistOutputDTO:
        self.logger.info("Registering extensionist with data: %s", data)
        
        use_case = RegisterUserExtensionistUseCase(self.auth_repository)
        user_entity = use_case.execute(data)
        
        return AuthMapper.to_user_extensionist_dto(user_entity)

    def upload_signing_image(self, user_id: int, image_data: bytes, image_content_type: str) -> str:
        self.logger.info("Uploading signing image for user: %s", user_id)
        
        use_case = UploadSigningImageUseCase(self.auth_repository)
        image_path = use_case.execute(user_id, image_data, image_content_type)
        
        return image_path
