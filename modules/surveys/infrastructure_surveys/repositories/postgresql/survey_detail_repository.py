from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional, Union

from modules.surveys.domain_surveys.repositories.survey_detail_repository import SurveyDetailRepository
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3
from common.infrastructure.database.models.survey import Survey1 as Survey1Model
from common.infrastructure.database.models.survey import Survey2 as Survey2Model
from common.infrastructure.database.models.survey import Survey3 as Survey3Model
from common.infrastructure.database.models.survey import ClassificationUser
from modules.surveys.infrastructure_surveys.mappers.survey1_mapper import Survey1Mapper
from modules.surveys.infrastructure_surveys.mappers.survey2_mapper import Survey2Mapper
from modules.surveys.infrastructure_surveys.mappers.survey3_mapper import Survey3Mapper

class PostgreSQLSurveyDetailRepository(SurveyDetailRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_survey_by_id_and_type(self, survey_id: int, survey_type: int) -> Optional[Union[Survey1, Survey2, Survey3]]:
        if survey_type == 1:
            stmt = select(Survey1Model).where(Survey1Model.id == survey_id)
            model = self.session.execute(stmt).scalar_one_or_none()
            return Survey1Mapper.to_entity(model) if model else None
        elif survey_type == 2:
            stmt = select(Survey2Model).where(Survey2Model.id == survey_id)
            model = self.session.execute(stmt).scalar_one_or_none()
            return Survey2Mapper.to_entity(model) if model else None
        elif survey_type == 3:
            stmt = select(Survey3Model).where(Survey3Model.id == survey_id)
            model = self.session.execute(stmt).scalar_one_or_none()
            return Survey3Mapper.to_entity(model) if model else None
        else:
            return None
        
    def get_classification_user_by_survey_id(self, survey_id: int, survey_type: int) -> Optional[dict]:
        if survey_type == 1:
            stmt = select(ClassificationUser).where(ClassificationUser.survey_idd1 == survey_id)
            model = self.session.execute(stmt).scalar_one_or_none()
            return model.data if model else None
        elif survey_type == 3:
            stmt = select(ClassificationUser).where(ClassificationUser.survey_idd3 == survey_id)
            model = self.session.execute(stmt).scalar_one_or_none()
            return model.data if model else None
        else:
            return None