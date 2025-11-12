from logging import Logger

from common.domain import (
    exceptions as common_exceptions,
    value_objects as common_value_objects,
)
from common.infrastructure.logging.config import get_logger

from modules.admin.domain_admin.repositories.admin_authentication_repository import (
    AdminAuthenticationRepository,
)
from modules.admin.domain_admin.entities.admin_user_entity import (
    AdminUser as AdminUserEntity,
)


_LOGGER: Logger = get_logger(__name__)


class LoginAdminUseCase:
    """
    Use case for admin user login.

    This encapsulates the business logic for admin user login,
    authenticating the user with email and password, and returning an
    authentication token.
    """

    def __init__(
        self,
        admin_authentication_repository: AdminAuthenticationRepository,
        secret_key: str,
    ) -> None:
        """
        Initialize the use case.

        Args:
            admin_authentication_repository (AdminAuthenticationRepository): Repository for admin authentication data access
            secret_key (str): JWT secret key for token generation
        """
        self._admin_authentication_repository: AdminAuthenticationRepository = (
            admin_authentication_repository
        )
        self._secret_key: str = secret_key

    def execute(
        self, email: str, password: str
    ) -> common_value_objects.AuthenticationToken:
        """
        Execute the login use case.

        Args:
            email (str): Admin user email
            password (str): Admin user password

        Returns:
            AuthenticationToken: JWT authentication token

        Raises:
            AuthenticationException: If authentication fails for any reason
        """
        _LOGGER.info(f"Attempting admin login for email: [{email}]")

        admin_user: AdminUserEntity | None = (
            self._admin_authentication_repository.find_admin_user_by_email_and_password(
                email=email, password=password
            )
        )

        if not admin_user:
            _LOGGER.error(
                f"Admin user with email [{email}] not found or invalid credentials"
            )
            raise common_exceptions.UserNotFoundException(
                0
            )  # Use a generic ID for admin login failure

        # Generate JWT token
        token_payload = {"user_id": admin_user.id}
        token = common_value_objects.AuthenticationToken.create_token(
            token_payload, self._secret_key
        )

        _LOGGER.info(f"Admin user [{admin_user.id}] logged in successfully")
        return token
