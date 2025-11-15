from sqlalchemy.orm import Session
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3
from modules.surveys.domain_surveys.repositories.survey3_repository import (
    Survey3Repository,
)
from modules.surveys.infrastructure_surveys.mappers.survey3_mapper import Survey3Mapper
from common.infrastructure.database.models.survey import Survey3 as Survey3Model


class PostgreSQLSurvey3Repository(Survey3Repository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, survey: Survey3) -> Survey3:
        survey_model = Survey3Mapper.to_db_model(survey)
        merged_model = self.session.merge(survey_model)
        self.session.commit()
        self.session.refresh(merged_model)
        return Survey3Mapper.to_entity(merged_model)

    def get_by_id(self, survey_id: int) -> Survey3 | None:
        survey_model = self.session.query(Survey3Model).filter_by(id=survey_id).first()
        if survey_model:
            return Survey3Mapper.to_entity(survey_model)
        return None
