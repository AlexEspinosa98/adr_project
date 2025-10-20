from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter as UserProducterEntity
from common.infrastructure.database.models.survey import UserProducter as UserProducterModel

class UserProducterMapper:
    @staticmethod
    def to_entity(model: UserProducterModel) -> UserProducterEntity:
        return UserProducterEntity(
            id=model.id,
            name=model.name,
            type_id=model.type_id,
            identification=model.identification,
            is_woman_rural=model.is_woman_rural,
            is_young_rural=model.is_young_rural,
            ethnic_belonging=model.ethnic_belonging,
            is_victim_conflict=model.is_victim_conflict,
            is_narp=model.is_narp,
        )