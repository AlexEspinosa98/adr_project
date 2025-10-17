from logging import Logger
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.repositories.survey1_repository import Survey1Repository
from modules.surveys.domain_surveys.repositories.user_producter_repository import UserProducterRepository
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.application_surveys.dtos.input_dto.create_survey1_input_dto import CreateSurvey1InputDTO
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class CreateSurvey1UseCase:
    def __init__(self, survey_repository: Survey1Repository, auth_repository: AuthRepository, user_producter_repository: UserProducterRepository):
        self._survey_repository = survey_repository
        self._auth_repository = auth_repository
        self._user_producter_repository = user_producter_repository

    def execute(self, input_dto: CreateSurvey1InputDTO, api_key: str, image_paths: list[str]) -> Survey1:
        _LOGGER.info(f"Creating new survey 1")

        extensionist = self._auth_repository.get_user_by_api_key(api_key)
        if not extensionist:
            raise Exception("Extensionist not found")

        producter = self._user_producter_repository.get_by_identification(input_dto.producter.identification)
        if not producter:
            producter_entity = UserProducter(**input_dto.producter.dict())
            producter = self._user_producter_repository.save(producter_entity)
            _LOGGER.info(f"Created new UserProducter with ID: {producter.id}")

        survey_entity = Survey1(
            id=0,
            extensionist_id=extensionist.id,
            user_producter_id=producter.id,
            property_id=input_dto.property_id,
            classification_user=input_dto.classification_user,
            medition_focalization=input_dto.medition_focalization,
            objetive_accompaniment=input_dto.objetive_accompaniment,
            initial_diagnosis=input_dto.initial_diagnosis,
            recommendations_commitments=input_dto.recommendations_commitments,
            observations=input_dto.observations,
            visit_date=input_dto.visit_date,
            attended_by=input_dto.attended_by,
            user=input_dto.user,
            worker_up=input_dto.worker_up,
            Household_size=input_dto.Household_size,
            other=input_dto.other,
            photo_user=image_paths[0] if len(image_paths) > 0 else None,
            photo_interaction=image_paths[1] if len(image_paths) > 1 else None,
            photo_panorama=image_paths[2] if len(image_paths) > 2 else None,
            phono_extra_1=image_paths[3] if len(image_paths) > 3 else None,
            state=input_dto.state
        )

        saved_survey = self._survey_repository.save(survey_entity)
        _LOGGER.info(f"Survey 1 created with ID: {saved_survey.id}")
        return saved_survey
