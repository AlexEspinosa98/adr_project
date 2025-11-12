from modules.admin.application_admin.dtos.output_dto.admin_user_dto import AdminUserDTO
from modules.admin.domain_admin.entities.admin_user_entity import (
    AdminUser as AdminUserEntity,
)


class AdminAuthenticationMapper:
    """
    Mapper for converting between admin domain objects and DTOs.

    This class handles the conversion logic, keeping DTOs as pure data structures
    and separating the mapping concerns from the domain and DTO classes.
    """

    @staticmethod
    def to_admin_user_dto(
        admin_user_entity: AdminUserEntity,
    ) -> AdminUserDTO:
        """
        Convert admin user entity to admin user DTO.

        Args:
            admin_user_entity (AdminUserEntity): Admin user domain entity

        Returns:
            AdminUserDTO: DTO for API response
        """
        return AdminUserDTO(
            id=admin_user_entity.id,
            email=admin_user_entity.email,
            name=admin_user_entity.name,
            last_name=admin_user_entity.last_name,
            phone=admin_user_entity.phone,
            rol=admin_user_entity.rol,
            identification=admin_user_entity.identification,
            created_at=admin_user_entity.created_at,
            updated_at=admin_user_entity.updated_at,
            is_active=admin_user_entity.is_active,
        )
