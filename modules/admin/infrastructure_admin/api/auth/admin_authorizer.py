from fastapi import Depends, Request

from common.infrastructure.api import decorators as common_decorators
from modules.admin.application_admin.dtos.output_dto.admin_user_dto import AdminUserDTO
from modules.admin.application_admin.services.admin_authentication_service import (
    AdminAuthenticationService,
)
from modules.admin.infrastructure_admin.services.admin_authentication_service_composer import (
    get_admin_authentication_service,
)


def _extract_token_from_request(request: Request) -> str:
    """Extract token from request headers."""
    return request.headers.get("Authorization", "")


@common_decorators.handle_authentication_exceptions
def get_current_admin_user(
    request: Request,
    auth_service: AdminAuthenticationService = Depends(
        get_admin_authentication_service
    ),
) -> AdminUserDTO:
    """
    Convenience function for getting current authenticated admin user.

    This is the main function that FastAPI routes should use for admin authentication.

    Args:
        request (Request): HTTP request
        auth_service (AdminAuthenticationService): Admin authentication service

    Returns:
        AdminUserDTO: Current authenticated admin user
    """
    raw_token = _extract_token_from_request(request=request)
    return auth_service.authenticate_admin_user_from_token(raw_token=raw_token)
