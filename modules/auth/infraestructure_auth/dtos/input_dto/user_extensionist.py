"""
Infrastructure DTOs for user extensionist operations.
"""

from typing import Any

from common.application import dtos as common_dtos
from common.domain import enums as common_enums


class UserExtensionistInputDTO(common_dtos.BaseDTO):
    """
    Infrastructure input DTO for user extensionist operations.
    Used by API endpoints.
    """
    name: str
    type_id: str
    identification: str
    city: str
    zone: str
    phone: str
    
    class Config:
        json_schema_extra: dict[str, dict[str, Any]] = {
            "example": {
                "name": "John Doe",
                "type_id": "cc",
                "identification": "123456789",
                "city": "Sample City",
                "zone": "Sample Zone",
                "phone": "123-456-7890"
            }
        }
