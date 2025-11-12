from sqlalchemy.orm import Session
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.repositories.survey2_repository import (
    Survey2Repository,
)
from modules.surveys.infrastructure_surveys.mappers.survey2_mapper import Survey2Mapper
from common.infrastructure.database.models.survey import Survey2 as Survey2Model


class PostgreSQLSurvey2Repository(Survey2Repository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, survey: Survey2) -> Survey2:
        survey_model = Survey2Mapper.to_db_model(survey)
        self.session.add(survey_model)
        self.session.commit()
        self.session.refresh(survey_model)
        return Survey2Mapper.to_entity(survey_model)

    def get_by_id(self, survey_id: int) -> Survey2 | None:
        survey_model = self.session.query(Survey2Model).filter_by(id=survey_id).first()
        if survey_model:
            return Survey2Mapper.to_entity(survey_model)
        return None
