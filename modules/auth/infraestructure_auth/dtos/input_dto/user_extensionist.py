"""
Infrastructure DTOs for user extensionist operations.
"""

from typing import Any, Optional

from common.application import dtos as common_dtos
from pydantic import EmailStr


class UserExtensionistInputDTO(common_dtos.BaseDTO):
    """
    Infrastructure input DTO for user extensionist operations.
    Used by API endpoints.
    """
    name: str
    email: EmailStr
    type_id: str
    identification: str
    city: str
    zone: str
    phone: str
    signig: Optional[str] = None
    
    class Config:
        json_schema_extra: dict[str, dict[str, Any]] = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "type_id": "cc",
                "identification": "123456789",
                "city": "Sample City",
                "zone": "Sample Zone",
                "phone": "123-456-7890",
                "signig": "base64_encoded_signature_or_url"
            }
        }