from typing import Optional

from pydantic import Field

from common.application import dtos as common_dtos


class AdminSurveyFilterInputDTO(common_dtos.BaseDTO):
    city: Optional[str] = Field(None, description="Filter surveys by city")
    extensionist: Optional[str] = Field(
        None, description="Filter surveys by extensionist name"
    )
