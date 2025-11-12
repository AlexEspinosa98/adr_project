from logging import Logger

from common.domain import exceptions as common_exceptions
from common.infrastructure.logging.config import get_logger

from modules.admin.domain_admin.repositories.admin_authentication_repository import (
    AdminAuthenticationRepository,
)
from modules.admin.domain_admin.entities.admin_user_entity import (
    AdminUser as AdminUserEntity,
)


_LOGGER: Logger = get_logger(__name__)


class RegisterAdminUseCase:
    """
    Use case for admin user registration.

    This encapsulates the business logic for admin user registration,
    validating the registration token, creating a new admin user, and returning
    the created admin user.
    """

    def __init__(
        self,
        admin_authentication_repository: AdminAuthenticationRepository,
        token_register_env: str,
    ) -> None:
        """
        Initialize the use case.

        Args:
            admin_authentication_repository (AdminAuthenticationRepository): Repository for admin authentication data access
            token_register_env (str): Registration token from environment variables
        """
        self._admin_authentication_repository: AdminAuthenticationRepository = (
            admin_authentication_repository
        )
        self._token_register_env: str = token_register_env

    def execute(
        self,
        name: str,
        last_name: str,
        email: str,
        password: str,
        phone: str,
        rol: str,
        identification: str,
        token_register: str,
    ) -> AdminUserEntity:
        """
        Execute the registration use case.

        Args:
            name (str): Admin user name
            last_name (str): Admin user last name
            email (str): Admin user email
            password (str): Admin user password
            phone (str): Admin user phone
            rol (str): Admin user role
            identification (str): Admin user identification
            token_register (str): Registration token provided by the user

        Returns:
            AdminUserEntity: The newly created admin user

        Raises:
            AuthenticationException: If registration fails for any reason
        """
        _LOGGER.info(f"Attempting admin registration for email: [{email}]")

        if token_register != self._token_register_env:
            _LOGGER.error("Invalid registration token provided")
            raise common_exceptions.AuthenticationException(
                "Invalid registration token"
            )

        existing_admin_user = (
            self._admin_authentication_repository.find_admin_user_by_email(email)
        )
        if existing_admin_user:
            _LOGGER.error(f"Admin user with email [{email}] already exists")
            raise common_exceptions.AuthenticationException(
                "Admin user with this email already exists"
            )

        new_admin_user = AdminUserEntity(
            name=name,
            last_name=last_name,
            email=email,
            password=password,  # Password should be hashed before saving
            phone=phone,
            rol=rol,
            identification=identification,
            token_register=token_register,
            is_active=True,  # New users are active by default
        )

        created_admin_user = self._admin_authentication_repository.save(new_admin_user)

        _LOGGER.info(f"Admin user [{created_admin_user.id}] registered successfully")
        return created_admin_user
