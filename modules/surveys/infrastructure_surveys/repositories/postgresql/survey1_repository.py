from sqlalchemy.orm import Session
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.repositories.survey1_repository import Survey1Repository
from modules.surveys.infrastructure_surveys.mappers.survey1_mapper import Survey1Mapper
from common.infrastructure.database.models.survey import Survey1 as Survey1Model

class PostgreSQLSurvey1Repository(Survey1Repository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, survey: Survey1) -> Survey1:
        survey_model = Survey1Mapper.to_db_model(survey)
        self.session.add(survey_model)
        self.session.commit()
        self.session.refresh(survey_model)
        return Survey1Mapper.to_entity(survey_model)
