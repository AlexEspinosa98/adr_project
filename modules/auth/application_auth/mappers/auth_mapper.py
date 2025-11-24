from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.application_auth.dtos.output_dto.register_user_extensionist import (
    RegisterUserExtensionistOutputDTO,
)
from modules.auth.application_auth.dtos.output_dto.update_user_extensionist import (
    UpdateUserExtensionistOutputDTO,
)
from modules.auth.application_auth.dtos.output_dto.login_user_extensionist_output_dto import (
    LoginUserExtensionistOutputDTO,
)


class AuthMapper:
    @staticmethod
    def to_user_extensionist_dto(
        user: UserExtensionist,
    ) -> RegisterUserExtensionistOutputDTO:
        return RegisterUserExtensionistOutputDTO(
            id=user.id,
            name=user.name,
            email=user.email,
            api_token=user.api_token,
        )

    @staticmethod
    def to_update_user_extensionist_dto(
        user: UserExtensionist,
    ) -> UpdateUserExtensionistOutputDTO:
        return UpdateUserExtensionistOutputDTO(
            name=user.name,
            email=user.email,
            phone=user.phone,
            city=user.city,
            zone=user.zone,
        )

    @staticmethod
    def to_login_user_extensionist_dto(
        user: UserExtensionist,
    ) -> LoginUserExtensionistOutputDTO:
        return LoginUserExtensionistOutputDTO(
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            type_id=user.type_id,
            identification=user.identification,
            city=user.city,
            zone=user.zone,
            api_token=user.api_token,
            signing_image_path=user.signing_image_path,
        )
