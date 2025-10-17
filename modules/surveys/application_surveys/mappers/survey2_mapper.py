from modules.surveys.domain_surveys.entities.survey2_entity import Survey2 as Survey2Entity
from modules.surveys.application_surveys.dtos.output_dto.create_survey2_output_dto import CreateSurvey2OutputDTO

class Survey2Mapper:
    @staticmethod
    def to_survey2_dto(survey_entity: Survey2Entity) -> CreateSurvey2OutputDTO:
        return CreateSurvey2OutputDTO(id=survey_entity.id)
