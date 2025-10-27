from pydantic import Field
from typing import Optional

from common.application import dtos as common_dtos


class AdminRegisterInputDTO(common_dtos.BaseDTO):
    """
    DTO for admin registration input.
    """

    name: str = Field(..., description="Admin user name")
    last_name: str = Field(..., description="Admin user last name")
    email: str = Field(..., description="Admin user email")
    password: str = Field(..., description="Admin user password")
    phone: Optional[str] = Field(None, description="Admin user phone")
    rol: Optional[str] = Field(None, description="Admin user role")
    identification: Optional[str] = Field(None, description="Admin user identification")
    token_register: str = Field(..., description="Admin registration token")
