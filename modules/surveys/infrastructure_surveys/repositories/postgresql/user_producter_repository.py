from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.repositories.user_producter_repository import UserProducterRepository
from common.infrastructure.database.models.survey import UserProducter as UserProducterModel
from modules.surveys.infrastructure_surveys.mappers.user_producter_mapper import UserProducterMapper

class PostgreSQLUserProducterRepository(UserProducterRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_identification(self, identification: str) -> Optional[UserProducter]:
        stmt = select(UserProducterModel).where(UserProducterModel.identification == identification)
        model = self.session.execute(stmt).scalar_one_or_none()
        return UserProducterMapper.to_entity(model) if model else None

    def save(self, producter: UserProducter) -> UserProducter:
        producter_model = UserProducterMapper.to_db_model(producter)
        self.session.add(producter_model)
        self.session.commit()
        self.session.refresh(producter_model)
        return UserProducterMapper.to_entity(producter_model)
