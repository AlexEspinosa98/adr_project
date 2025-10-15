from logging import Logger
from modules.surveys.application_surveys.dtos.input_dto.create_survey1 import CreateSurvey1InputDTO
from modules.surveys.application_surveys.dtos.output_dto.create_survey1 import CreateSurvey1OutputDTO
from modules.surveys.application_surveys.mappers.survey1_mapper import Survey1Mapper
from modules.surveys.application_surveys.use_cases.create_survey1 import CreateSurvey1UseCase
from modules.surveys.domain_surveys.repositories.survey1_repository import Survey1Repository
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class Survey1Service:
    def __init__(self, survey_repository: Survey1Repository):
        self.logger = _LOGGER
        self.survey_repository = survey_repository

    def create_survey1(self, data: CreateSurvey1InputDTO) -> CreateSurvey1OutputDTO:
        self.logger.info("Creating survey 1 with data: %s", data)
        
        use_case = CreateSurvey1UseCase(self.survey_repository)
        survey_entity = use_case.execute(data)
        
        return Survey1Mapper.to_survey1_dto(survey_entity)
