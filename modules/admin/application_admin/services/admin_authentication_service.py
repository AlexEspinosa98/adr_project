from logging import Logger

from modules.admin.application_admin.mappers.admin_authentication_mapper import AdminAuthenticationMapper
from modules.admin.application_admin.dtos.output_dto.admin_user_dto import AdminUserDTO
from modules.admin.application_admin.use_cases.authenticate_admin_user import (
    AuthenticateAdminUserUseCase,
)
from modules.admin.domain_admin.aggregates.admin_authentication_aggregate import AdminAuthenticationAggregate
from modules.admin.domain_admin.repositories.admin_authentication_repository import AdminAuthenticationRepository

from common.infrastructure.logging.config import get_logger


_LOGGER: Logger = get_logger(__name__)


class AdminAuthenticationService:
    """
    Application service for admin authentication operations.

    Orchestrates authentication use cases and coordinates domain operations.
    This is the main entry point for authentication from the infrastructure layer.
    """

    def __init__(
        self,
        admin_authentication_repository: AdminAuthenticationRepository,
        secret_key: str,
    ) -> None:
        """
        Initialize the authentication service.

        Args:
            admin_authentication_repository (AdminAuthenticationRepository): Repository for admin authentication data access
            secret_key (str): JWT secret key for token validation
        """
        self._admin_authentication_repository: AdminAuthenticationRepository = admin_authentication_repository
        self._secret_key: str = secret_key
        self._authenticate_admin_user_use_case = AuthenticateAdminUserUseCase(
            admin_authentication_repository, secret_key
        )
        self._mapper = AdminAuthenticationMapper()

    def authenticate_admin_user_from_token(
        self, raw_token: str
    ) -> AdminUserDTO:
        """
        Authenticate an admin user from a JWT token and return user information.
        This is the main method that infrastructure will call to authenticate admin users.

        Args:
            raw_token (str): Raw JWT token from request headers

        Returns:
            AdminUserDTO: Authenticated admin user information

        Raises:
            AuthenticationException: If authentication fails for any reason
        """
        auth_result: AdminAuthenticationAggregate = (
            self._authenticate_admin_user_use_case.execute(raw_token=raw_token)
        )

        return self._mapper.to_admin_user_dto(auth_result.user)

    def authenticate_admin_user_from_token_optional(
        self, raw_token: str | None = None
    ) -> AdminUserDTO | None:
        """
        Optional authentication - returns None if token is not provided or invalid.

        Useful for endpoints that support both authenticated and anonymous access.

        Args:
            raw_token (Optional[str]): Raw JWT token from request headers

        Returns:
            Optional[AdminUserDTO]: User info if valid token, None otherwise
        """
        if not raw_token:
            return None

        return self.authenticate_admin_user_from_token(raw_token=raw_token)
