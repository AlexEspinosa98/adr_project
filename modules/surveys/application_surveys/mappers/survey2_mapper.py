from modules.surveys.application_surveys.dtos.output_dto.create_survey2_output_dto import (
    CreateSurvey2OutputDTO,
)
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2


class Survey2Mapper:
    @staticmethod
    def to_survey2_dto(entity: Survey2) -> CreateSurvey2OutputDTO:
        return CreateSurvey2OutputDTO(id=entity.id)
