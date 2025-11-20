from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from modules.surveys.domain_surveys.entities.survey_rejection_entity import SurveyRejection
from modules.surveys.domain_surveys.repositories.survey_rejection_repository import SurveyRejectionRepository
from common.infrastructure.database.models.survey import SurveyRejection as SurveyRejectionModel
from modules.surveys.infrastructure_surveys.mappers.survey_rejection_mapper import SurveyRejectionMapper


class PostgreSQLSurveyRejectionRepository(SurveyRejectionRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, survey_rejection: SurveyRejection) -> SurveyRejection:
        survey_rejection_model = SurveyRejectionMapper.to_db_model(survey_rejection)
        self.session.add(survey_rejection_model)
        self.session.commit()
        self.session.refresh(survey_rejection_model)
        return SurveyRejectionMapper.to_entity(survey_rejection_model)

    def get_by_survey_id_and_type(self, survey_id: int, survey_type: int) -> Optional[SurveyRejection]:
        stmt = select(SurveyRejectionModel).where(
            SurveyRejectionModel.survey_id == survey_id,
            SurveyRejectionModel.survey_type == survey_type
        ).order_by(SurveyRejectionModel.created_at.desc())
        model = self.session.execute(stmt).first()
        return SurveyRejectionMapper.to_entity(model[0]) if model else None