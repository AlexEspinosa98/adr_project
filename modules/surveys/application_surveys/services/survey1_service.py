from logging import Logger
from modules.surveys.application_surveys.dtos.input_dto.create_survey1_input_dto import (
    CreateSurvey1InputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.create_survey1_output_dto import (
    CreateSurvey1OutputDTO,
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
from modules.surveys.application_surveys.dtos.photo_paths_dto import (
    SurveyPhotoPathsDTO,
)
from modules.surveys.application_surveys.mappers.survey1_mapper import Survey1Mapper
from modules.surveys.application_surveys.use_cases.create_survey1_use_case import (
    CreateSurvey1UseCase,
)
from modules.surveys.domain_surveys.repositories.survey1_repository import (
    Survey1Repository,
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


class Survey1Service:
    def __init__(
        self,
        survey_repository: Survey1Repository,
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

    def create_survey1(
        self,
        data: CreateSurvey1InputDTO,
        producter_input_dto: SurveyUserProducterInputDTO,
        property_info_input_dto: PropertyInfoInputDTO,
        classification_user_input_dto: ClassificationUserInputDTO,
        api_key: str,
        photo_paths: SurveyPhotoPathsDTO,
    ) -> CreateSurvey1OutputDTO:
        self.logger.info("Creating survey 1 with data: %s", data)

        use_case = CreateSurvey1UseCase(
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

        return Survey1Mapper.to_survey1_dto(survey_entity)
