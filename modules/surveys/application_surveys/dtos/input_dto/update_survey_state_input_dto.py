from pydantic import BaseModel
from typing import Literal


class UpdateSurveyStateInputDTO(BaseModel):
    new_state: Literal["ACCEPTED", "REJECTED"]
