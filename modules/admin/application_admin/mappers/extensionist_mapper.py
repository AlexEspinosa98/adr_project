from modules.admin.application_admin.dtos.output_dto.extensionist_output_dto import (
    ExtensionistOutputDTO,
)
from modules.admin.domain_admin.entities.extensionist_user_entity import (
    ExtensionistUser,
)


class ExtensionistMapper:
    @staticmethod
    def to_extensionist_output_dto(
        extensionist_user_entity: ExtensionistUser,
    ) -> ExtensionistOutputDTO:
        """
        Convert extensionist user entity to extensionist output DTO.
        """
        return ExtensionistOutputDTO(
            id=extensionist_user_entity.id,
            email=extensionist_user_entity.email,
            name=extensionist_user_entity.name,
            phone=extensionist_user_entity.phone,
            identification=extensionist_user_entity.identification,
            city=extensionist_user_entity.city,
            zone=extensionist_user_entity.zone,
        )
