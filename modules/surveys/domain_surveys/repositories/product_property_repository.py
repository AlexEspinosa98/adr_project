from abc import ABC, abstractmethod
from typing import Optional
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)


class ProductPropertyRepository(ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[ProductProperty]:
        pass

    @abstractmethod
    def get_by_id(self, property_id: int) -> Optional[ProductProperty]:
        pass

    @abstractmethod
    def save(self, property: ProductProperty) -> ProductProperty:
        pass
