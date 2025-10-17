from modules.auth.domain_auth.entities.auth_entities import UserProducter as UserProducterEntity
from common.infrastructure.database.models.auth import UserProducter as UserProducterModel

class UserProducterMapper:
    @staticmethod
    def to_db_model(entity: UserProducterEntity) -> UserProducterModel:
        return UserProducterModel(**entity.dict())

    @staticmethod
    def to_entity(model: UserProducterModel) -> UserProducterEntity:
        return UserProducterEntity(**model.__dict__)
