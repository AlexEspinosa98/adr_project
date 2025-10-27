from datetime import datetime
from typing import Optional

from common.application import dtos as common_dtos
from common.domain import enums as common_enums
from pydantic import Field


class AdminUserDTO(common_dtos.BaseDTO):
    """
    DTO for admin user information.

    Contains only the necessary information for API responses
    without exposing internal domain structure.

    This is a pure data structure - no business logic here.
    """

    id: int
    email: str
    name: str
    last_name: str
    phone: Optional[str]
    rol: Optional[str]
    identification: Optional[str]
    created_at: datetime
    updated_at: datetime
    is_active: bool
