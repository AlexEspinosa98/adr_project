from modules.surveys.domain_surveys.entities.survey3_entity import Survey3
from modules.surveys.application_surveys.dtos.output_dto.create_survey3_output_dto import (
    CreateSurvey3OutputDTO,
)


class Survey3Mapper:
    @staticmethod
    def to_survey3_dto(entity: Survey3) -> CreateSurvey3OutputDTO:
        return CreateSurvey3OutputDTO(id=entity.id)
