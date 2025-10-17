from modules.surveys.domain_surveys.entities.survey1_entity import Survey1 as Survey1Entity
from modules.surveys.application_surveys.dtos.output_dto.create_survey1_output_dto import CreateSurvey1OutputDTO

class Survey1Mapper:
    @staticmethod
    def to_survey1_dto(survey_entity: Survey1Entity) -> CreateSurvey1OutputDTO:
        return CreateSurvey1OutputDTO(id=survey_entity.id)