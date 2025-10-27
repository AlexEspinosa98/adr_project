from pydantic import Field

from common.application import dtos as common_dtos


class AdminLoginOutputDTO(common_dtos.BaseDTO):
    """
    DTO for admin login output.
    """

    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field("bearer", description="Type of token")
