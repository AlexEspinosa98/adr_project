from logging import Logger
from modules.surveys.application_surveys.dtos.input_dto.create_survey3_input_dto import (
    CreateSurvey3InputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.create_survey3_output_dto import (
    CreateSurvey3OutputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.survey_user_producter import (
    SurveyUserProducterInputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.property_info_input_dto import (
    PropertyInfoInputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.classification_user_input_dto import (
    ClassificationUserInputDTO,
)
from modules.surveys.application_surveys.mappers.survey3_mapper import Survey3Mapper
from modules.surveys.application_surveys.use_cases.create_survey3_use_case import (
    CreateSurvey3UseCase,
)
from modules.surveys.application_surveys.dtos.photo_paths_dto import (
    SurveyPhotoPathsDTO,
)
from modules.surveys.domain_surveys.repositories.survey3_repository import (
    Survey3Repository,
)
from modules.surveys.domain_surveys.repositories.user_producter_repository import (
    UserProducterRepository,
)
from modules.surveys.domain_surveys.repositories.product_property_repository import (
    ProductPropertyRepository,
)
from modules.surveys.domain_surveys.repositories.classification_user_repository import (
    ClassificationUserRepository,
)
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)


class Survey3Service:
    def __init__(
        self,
        survey_repository: Survey3Repository,
        auth_repository: AuthRepository,
        user_producter_repository: UserProducterRepository,
        product_property_repository: ProductPropertyRepository,
        classification_user_repository: ClassificationUserRepository,
    ):
        self.logger = _LOGGER
        self.survey_repository = survey_repository
        self.auth_repository = auth_repository
        self.user_producter_repository = user_producter_repository
        self.product_property_repository = product_property_repository
        self.classification_user_repository = classification_user_repository

    def create_survey3(
        self,
        data: CreateSurvey3InputDTO,
        producter_input_dto: SurveyUserProducterInputDTO,
        property_info_input_dto: PropertyInfoInputDTO,
        classification_user_input_dto: ClassificationUserInputDTO,
        api_key: str,
        photo_paths: SurveyPhotoPathsDTO,
    ) -> CreateSurvey3OutputDTO:
        self.logger.info("Creating survey 3 with data: %s", data)

        use_case = CreateSurvey3UseCase(
            self.survey_repository,
            self.auth_repository,
            self.user_producter_repository,
            self.product_property_repository,
            self.classification_user_repository,
        )
        survey_entity = use_case.execute(
            data,
            producter_input_dto,
            property_info_input_dto,
            classification_user_input_dto,
            api_key,
            photo_paths,
        )

        return Survey3Mapper.to_survey3_dto(survey_entity)
