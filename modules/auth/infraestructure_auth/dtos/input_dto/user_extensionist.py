"""
Infrastructure DTOs for user extensionist operations.
"""

from typing import Any

from common.application import dtos as common_dtos


class UserExtensionistInputDTO(common_dtos.BaseDTO):
    """
    Infrastructure input DTO for user extensionist operations.
    Used by API endpoints.
    """

    name: str
    email: str
    type_id: str
    identification: str
    city: str
    zone: str
    phone: str
    password: str

    class Config:
        json_schema_extra: dict[str, dict[str, Any]] = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "password": "SecretPassword123",
                "type_id": "cc",
                "identification": "123456789",
                "city": "Sample City",
                "zone": "Sample Zone",
                "phone": "123-456-7890",
            }
        }
