from modules.surveys.domain_surveys.entities.survey_rejection_entity import SurveyRejection as SurveyRejectionEntity
from common.infrastructure.database.models.survey import SurveyRejection as SurveyRejectionModel


class SurveyRejectionMapper:
    @staticmethod
    def to_entity(model: SurveyRejectionModel) -> SurveyRejectionEntity:
        return SurveyRejectionEntity(
            id=model.id,
            survey_id=model.survey_id,
            survey_type=model.survey_type,
            reason=model.reason,
            admin_user_id=model.admin_user_id,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_db_model(entity: SurveyRejectionEntity) -> SurveyRejectionModel:
        return SurveyRejectionModel(
            id=entity.id if entity.id != 0 else None,
            survey_id=entity.survey_id,
            survey_type=entity.survey_type,
            reason=entity.reason,
            admin_user_id=entity.admin_user_id,
        )
