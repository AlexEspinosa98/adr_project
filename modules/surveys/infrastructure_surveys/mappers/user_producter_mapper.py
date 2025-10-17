from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter as UserProducterEntity
from common.infrastructure.database.models.survey import UserProducter as UserProducterModel

class UserProducterMapper:
    @staticmethod
    def to_db_model(entity: UserProducterEntity) -> UserProducterModel:
        return UserProducterModel(**entity.dict())

    @staticmethod
    def to_entity(model: UserProducterModel) -> UserProducterEntity:
        return UserProducterEntity(**model.__dict__)
