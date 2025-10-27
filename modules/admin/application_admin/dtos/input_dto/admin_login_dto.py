from pydantic import Field

from common.application import dtos as common_dtos


class AdminLoginInputDTO(common_dtos.BaseDTO):
    """
    DTO for admin login input.
    """

    email: str = Field(..., description="Admin user email")
    password: str = Field(..., description="Admin user password")
