from typing import Any

from common.domain import (
    aggregates as common_aggregates,
    exceptions as common_exceptions,
    value_objects as common_value_objects,
)
from modules.admin.domain_admin.entities.admin_user_entity import AdminUser as AdminUserEntity


class AdminAuthenticationAggregate(common_aggregates.BaseAggregate):
    """
    Aggregate representing the result of an admin authentication process.

    This is the root aggregate that ensures consistency between
    the token and the authenticated admin user. It enforces business invariants
    and manages the authentication lifecycle.
    """

    user: AdminUserEntity
    token: common_value_objects.AuthenticationToken

    def get_aggregate_id(self) -> Any:
        """The aggregate is identified by the user ID."""
        return self.user.get_identity()

    def validate_invariants(self) -> None:
        """
        Validate business invariants for authentication.
        """
        if not self.user.is_active:
            raise common_exceptions.InvalidUserStatusException(
                self.user.get_identity(), "inactive"
            )

    def model_post_init(self, __context: Any) -> None:
        """Validate invariants after model creation."""
        self.validate_invariants()

    def is_valid(self) -> bool:
        """Check if this authentication result is valid."""
        try:
            self.validate_invariants()
            return True
        except Exception:
            return False

    def get_user_id(self) -> int:
        """Get the user ID as integer for compatibility."""
        return self.user.id

    def refresh_authentication(self) -> None:
        """
        Refresh the authentication (update last login, etc.).
        This is a domain operation that maintains consistency.
        """
        self.user.mark_as_updated()
        self.validate_invariants()
