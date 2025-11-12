from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty as ProductPropertyEntity,
)
from common.infrastructure.database.models.survey import (
    ProductProperty as ProductPropertyModel,
)


class ProductPropertyMapper:
    @staticmethod
    def to_entity(model: ProductPropertyModel) -> ProductPropertyEntity:
        return ProductPropertyEntity(
            id=model.id,
            name=model.name,
            latitude=model.latitude,
            longitude=model.longitude,
            asnm=model.asnm,
            state=model.state,
            city=model.city,
            village=model.village,
            linea_productive_primary=model.linea_productive_primary,
            linea_productive_secondary=model.linea_productive_secondary,
            area_in_production=model.area_in_production,
        )

    @staticmethod
    def to_db_model(entity: ProductPropertyEntity) -> ProductPropertyModel:
        return ProductPropertyModel(
            id=entity.id if entity.id != 0 else None,
            name=entity.name,
            latitude=entity.latitude,
            longitude=entity.longitude,
            asnm=entity.asnm,
            state=entity.state,
            city=entity.city,
            village=entity.village,
            linea_productive_primary=entity.linea_productive_primary,
            linea_productive_secondary=entity.linea_productive_secondary,
            area_in_production=entity.area_in_production,
        )
