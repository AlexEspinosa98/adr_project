from modules.surveys.domain_surveys.entities.product_property_entity import ProductProperty as ProductPropertyEntity
from common.infrastructure.database.models.survey import ProductProperty as ProductPropertyModel

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
            total_area=model.total_area,
            linea_productive_primary=model.linea_productive_primary,
            area_total_linea_productive_primary=model.area_total_linea_productive_primary,
            linea_productive_secondary=model.linea_productive_secondary,
            area_total_linea_productive_secondary=model.area_total_linea_productive_secondary,
            area_in_production=model.area_in_production,
        )