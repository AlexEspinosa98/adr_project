from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.application_auth.dtos.output_dto.register_user_extensionist import RegisterUserExtensionistOutputDTO

class AuthMapper:
    @staticmethod
    def to_user_extensionist_dto(user: UserExtensionist) -> RegisterUserExtensionistOutputDTO:
        return RegisterUserExtensionistOutputDTO(
            id=user.id,
            name=user.name,
            email=user.email,
            api_token=user.api_token,
        )

    @staticmethod
    def to_update_user_extensionist_dto(user: UserExtensionist) -> UpdateUserExtensionistOutputDTO:
        return UpdateUserExtensionistOutputDTO(
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            city=user.city,
            zone=user.zone,
        )
