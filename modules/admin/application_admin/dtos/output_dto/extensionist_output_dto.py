from typing import Optional

from common.application import dtos as common_dtos


class ExtensionistOutputDTO(common_dtos.BaseDTO):
    """
    DTO for extensionist user information.
    """

    id: int
    name: Optional[str]
    identification: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    city: Optional[str]
    zone: Optional[str]
