from sqlalchemy.orm import Session
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.repositories.survey1_repository import (
    Survey1Repository,
)
from modules.surveys.infrastructure_surveys.mappers.survey1_mapper import Survey1Mapper
from common.infrastructure.database.models.survey import Survey1 as Survey1Model


class PostgreSQLSurvey1Repository(Survey1Repository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, survey: Survey1) -> Survey1:
        survey_model = Survey1Mapper.to_db_model(survey)

        if survey_model.id:  # Si tiene ID, se asume que ya existe -> actualizar
            existing_survey = self.session.get(Survey1Model, survey_model.id)
            if existing_survey:
                for key, value in survey_model.__dict__.items():
                    if key != "_sa_instance_state":
                        setattr(existing_survey, key, value)
                self.session.commit()
                self.session.refresh(existing_survey)
                return Survey1Mapper.to_entity(existing_survey)

        # Si no tiene ID, crear nuevo
        self.session.add(survey_model)
        self.session.commit()
        self.session.refresh(survey_model)
        return Survey1Mapper.to_entity(survey_model)

    def get_by_id(self, survey_id: int) -> Survey1 | None:
        survey_model = self.session.query(Survey1Model).filter_by(id=survey_id).first()
        if survey_model:
            return Survey1Mapper.to_entity(survey_model)
        return None
