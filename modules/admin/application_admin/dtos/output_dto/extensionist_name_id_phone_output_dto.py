from typing import Optional

from common.application import dtos as common_dtos


class ExtensionistNameIdPhoneOutputDTO(common_dtos.BaseDTO):
    """
    DTO for extensionist name, identification, and phone information.
    """

    id: int
    name: Optional[str]
    identification: Optional[str]
    phone: Optional[str]
