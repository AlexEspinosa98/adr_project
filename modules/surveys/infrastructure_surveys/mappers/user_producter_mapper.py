from modules.surveys.domain_surveys.entities.user_producter_entity import (
    UserProducter as UserProducterEntity,
)
from common.infrastructure.database.models.survey import (
    UserProducter as UserProducterModel,
)


class UserProducterMapper:
    @staticmethod
    def to_entity(model: UserProducterModel) -> UserProducterEntity:
        return UserProducterEntity(
            id=model.id,
            name=model.name,
            type_id=model.type_id,
            identification=model.identification,
            number_phone=model.number_phone,
            is_woman_rural=model.is_woman_rural,
            is_young_rural=model.is_young_rural,
            ethnic_belonging=model.ethnic_belonging,
            is_victim_conflict=model.is_victim_conflict,
            is_narp=model.is_narp,
            is_producer_organization_member=model.is_producer_organization_member,
            organization_name=model.organization_name,
            representantive1_name=model.representantive1_name,
        )

    @staticmethod
    def to_db_model(entity: UserProducterEntity) -> UserProducterModel:
        return UserProducterModel(
            id=entity.id if entity.id != 0 else None,
            name=entity.name,
            type_id=entity.type_id,
            identification=entity.identification,
            number_phone=entity.number_phone,
            is_woman_rural=entity.is_woman_rural,
            is_young_rural=entity.is_young_rural,
            ethnic_belonging=entity.ethnic_belonging,
            is_victim_conflict=entity.is_victim_conflict,
            is_narp=entity.is_narp,
            is_producer_organization_member=entity.is_producer_organization_member,
            organization_name=entity.organization_name,
            representantive1_name=entity.representantive1_name,
        )
