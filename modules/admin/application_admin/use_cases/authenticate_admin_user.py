from logging import Logger

from pydantic import ValidationError

from common.domain import (
    exceptions as common_exceptions,
    value_objects as common_value_objects,
)
from common.infrastructure.logging.config import get_logger

from modules.admin.domain_admin.aggregates.admin_authentication_aggregate import (
    AdminAuthenticationAggregate,
)
from modules.admin.domain_admin.repositories.admin_authentication_repository import (
    AdminAuthenticationRepository,
)
from modules.admin.domain_admin.entities.admin_user_entity import (
    AdminUser as AdminUserEntity,
)


_LOGGER: Logger = get_logger(__name__)


class AuthenticateAdminUserUseCase:
    """
    Use case for authenticating an admin user from a JWT token.

    This encapsulates the business logic for admin user authentication,
    ensuring all domain rules are enforced and returning a proper
    authentication result aggregate.
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
            secret_key (str): JWT secret key for token validation
        """
        self._admin_authentication_repository: AdminAuthenticationRepository = (
            admin_authentication_repository
        )
        self._secret_key: str = secret_key

    def execute(self, raw_token: str) -> AdminAuthenticationAggregate:
        """
        Execute the authentication use case.

        Args:
            raw_token (str): Raw JWT token from request

        Returns:
            AdminAuthenticationAggregate: Complete authentication result

        Raises:
            Various AuthenticationExceptions: If authentication fails at any step
        """
        _LOGGER.info("Creating AuthenticationToken from raw token")
        try:
            token = common_value_objects.AuthenticationToken(raw_token=raw_token)
        except ValidationError as e:
            _LOGGER.error(f"Invalid token format: [{e}]")
            raise common_exceptions.InvalidTokenException(
                f"The provided token format is invalid: [{e}]"
            )

        _LOGGER.info("Extracting user ID from token")
        user_id: int = token.extract_user_id(secret_key=self._secret_key)

        _LOGGER.info(f"Finding admin user by ID: [{user_id}]")
        admin_user: AdminUserEntity | None = (
            self._admin_authentication_repository.find_active_admin_user_by_id(
                user_id=user_id
            )
        )

        if not admin_user:
            _LOGGER.error(f"Admin user with ID [{user_id}] not found or not active")
            raise common_exceptions.UserNotFoundException(user_id)

        _LOGGER.info(
            f"Admin user [{admin_user.get_identity()}] authenticated successfully"
        )
        return AdminAuthenticationAggregate(user=admin_user, token=token)
