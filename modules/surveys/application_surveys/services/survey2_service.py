from logging import Logger
from modules.surveys.application_surveys.dtos.input_dto.create_survey2_input_dto import (
    CreateSurvey2InputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.create_survey2_output_dto import (
    CreateSurvey2OutputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.survey_user_producter import (
    SurveyUserProducterInputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.property_info_input_dto import (
    PropertyInfoInputDTO,
)
from modules.surveys.application_surveys.mappers.survey2_mapper import Survey2Mapper
from modules.surveys.application_surveys.use_cases.create_survey2_use_case import (
    CreateSurvey2UseCase,
)
from modules.surveys.application_surveys.dtos.photo_paths_dto import (
    SurveyPhotoPathsDTO,
)
from modules.surveys.domain_surveys.repositories.survey2_repository import (
    Survey2Repository,
)
from modules.surveys.domain_surveys.repositories.user_producter_repository import (
    UserProducterRepository,
)
from modules.surveys.domain_surveys.repositories.product_property_repository import (
    ProductPropertyRepository,
)
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)


class Survey2Service:
    def __init__(
        self,
        survey_repository: Survey2Repository,
        auth_repository: AuthRepository,
        user_producter_repository: UserProducterRepository,
        product_property_repository: ProductPropertyRepository,
    ):
        self.logger = _LOGGER
        self.survey_repository = survey_repository
        self.auth_repository = auth_repository
        self.user_producter_repository = user_producter_repository
        self.product_property_repository = product_property_repository

    def create_survey2(
        self,
        data: CreateSurvey2InputDTO,
        producter_input_dto: SurveyUserProducterInputDTO,
        property_info_input_dto: PropertyInfoInputDTO,
        api_key: str,
        photo_paths: SurveyPhotoPathsDTO,
    ) -> CreateSurvey2OutputDTO:
        self.logger.info("Creating survey 2 with data: %s", data)

        use_case = CreateSurvey2UseCase(
            self.survey_repository,
            self.auth_repository,
            self.user_producter_repository,
            self.product_property_repository,
        )
        survey_entity = use_case.execute(
            data, producter_input_dto, property_info_input_dto, api_key, photo_paths
        )

        return Survey2Mapper.to_survey2_dto(survey_entity)
