from modules.auth.domain_auth.entities.auth_entities import ProductProperty as ProductPropertyEntity
from common.infrastructure.database.models.auth import ProductProperty as ProductPropertyModel

class ProductPropertyMapper:
    @staticmethod
    def to_db_model(entity: ProductPropertyEntity) -> ProductPropertyModel:
        return ProductPropertyModel(**entity.dict())

    @staticmethod
    def to_entity(model: ProductPropertyModel) -> ProductPropertyEntity:
        return ProductPropertyEntity(**model.__dict__)
