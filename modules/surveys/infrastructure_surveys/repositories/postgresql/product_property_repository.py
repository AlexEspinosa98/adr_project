from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from modules.surveys.domain_surveys.entities.product_property_entity import ProductProperty
from modules.surveys.domain_surveys.repositories.product_property_repository import ProductPropertyRepository
from common.infrastructure.database.models.survey import ProductProperty as ProductPropertyModel
from modules.surveys.infrastructure_surveys.mappers.product_property_mapper import ProductPropertyMapper

class PostgreSQLProductPropertyRepository(ProductPropertyRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_name(self, name: str) -> Optional[ProductProperty]:
        stmt = select(ProductPropertyModel).where(ProductPropertyModel.name == name)
        model = self.session.execute(stmt).scalar_one_or_none()
        return ProductPropertyMapper.to_entity(model) if model else None

    def save(self, property: ProductProperty) -> ProductProperty:
        property_model = ProductPropertyMapper.to_db_model(property)
        self.session.add(property_model)
        self.session.commit()
        self.session.refresh(property_model)
        return ProductPropertyMapper.to_entity(property_model)
