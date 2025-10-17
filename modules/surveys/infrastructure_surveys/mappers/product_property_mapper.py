from modules.surveys.domain_surveys.entities.product_property_entity import ProductProperty as ProductPropertyEntity
from common.infrastructure.database.models.survey import ProductProperty as ProductPropertyModel

class ProductPropertyMapper:
    @staticmethod
    def to_db_model(entity: ProductPropertyEntity) -> ProductPropertyModel:
        return ProductPropertyModel(**entity.dict())

    @staticmethod
    def to_entity(model: ProductPropertyModel) -> ProductPropertyEntity:
        return ProductPropertyEntity(**model.__dict__)
