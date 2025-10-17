from logging import Logger
from modules.surveys.application_surveys.dtos.input_dto.create_survey3_input_dto import CreateSurvey3InputDTO
from modules.surveys.application_surveys.dtos.output_dto.create_survey3_output_dto import CreateSurvey3OutputDTO
from modules.surveys.application_surveys.mappers.survey3_mapper import Survey3Mapper
from modules.surveys.application_surveys.use_cases.create_survey3_use_case import CreateSurvey3UseCase
from modules.surveys.domain_surveys.repositories.survey3_repository import Survey3Repository
from modules.surveys.domain_surveys.repositories.user_producter_repository import UserProducterRepository
from modules.surveys.domain_surveys.repositories.product_property_repository import ProductPropertyRepository
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class Survey3Service:
    def __init__(self, survey_repository: Survey3Repository, auth_repository: AuthRepository, user_producter_repository: UserProducterRepository, product_property_repository: ProductPropertyRepository):
        self.logger = _LOGGER
        self.survey_repository = survey_repository
        self.auth_repository = auth_repository
        self.user_producter_repository = user_producter_repository
        self.product_property_repository = product_property_repository

    def create_survey3(self, data: CreateSurvey3InputDTO, api_key: str, image_paths: list[str]) -> CreateSurvey3OutputDTO:
        self.logger.info("Creating survey 3 with data: %s", data)
        
        use_case = CreateSurvey3UseCase(self.survey_repository, self.auth_repository, self.user_producter_repository, self.product_property_repository)
        survey_entity = use_case.execute(data, api_key, image_paths)
        
        return Survey3Mapper.to_survey3_dto(survey_entity)
