from logging import Logger
import os
import uuid
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)
IMAGE_DIR = "images/signing"

class UploadSigningImageUseCase:
    def __init__(self, auth_repository: AuthRepository):
        self._auth_repository = auth_repository

    def execute(self, user_id: int, image_data: bytes, image_content_type: str) -> str:
        _LOGGER.info(f"Uploading signing image for user with ID: {user_id}")

        user = self._auth_repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")

        if not os.path.exists(IMAGE_DIR):
            os.makedirs(IMAGE_DIR)
            
        file_extension = image_content_type.split("/")[-1]
        if not file_extension:
            file_extension = "png" # default
            
        image_filename = f"{uuid.uuid4()}.{file_extension}"
        image_path = os.path.join(IMAGE_DIR, image_filename)

        with open(image_path, "wb") as f:
            f.write(image_data)

        user.signing_image_path = image_path
        self._auth_repository.update_extensionist(user)

        _LOGGER.info(f"Signing image uploaded for user {user_id} to {image_path}")
        return image_path
