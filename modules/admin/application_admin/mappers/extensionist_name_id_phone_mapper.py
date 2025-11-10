from modules.admin.application_admin.dtos.output_dto.extensionist_name_id_phone_output_dto import (
    ExtensionistNameIdPhoneOutputDTO,
)
from modules.admin.domain_admin.entities.extensionist_user_entity import (
    ExtensionistUser,
)


class ExtensionistNameIdPhoneMapper:
    @staticmethod
    def to_extensionist_name_id_phone_output_dto(
        extensionist_user_entity: ExtensionistUser,
    ) -> ExtensionistNameIdPhoneOutputDTO:
        """
        Convert extensionist user entity to extensionist name, identification, and phone DTO.
        """
        return ExtensionistNameIdPhoneOutputDTO(
            id=extensionist_user_entity.id,
            name=extensionist_user_entity.name,
            identification=extensionist_user_entity.identification,
            phone=extensionist_user_entity.phone,
        )
