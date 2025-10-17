from typing import Optional
from common.domain import entities as common_entities
from pydantic import Field

class ProductProperty(common_entities.BaseEntity):
    name: Optional[str] = Field(None, description="Product property name")
