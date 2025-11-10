from typing import Optional

from common.domain import entities as common_entities


class ExtensionistUser(common_entities.BaseEntity):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    type_id: Optional[int]
    identification: Optional[str]
    city: Optional[str]
    zone: Optional[str]
    signing_image_path: Optional[str]
    api_token: Optional[str]
