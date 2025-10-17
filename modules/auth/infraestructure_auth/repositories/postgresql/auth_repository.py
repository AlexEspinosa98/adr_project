from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from modules.auth.domain_auth.entities.auth_entities import UserExtensionist, UserProducter
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from common.infrastructure.database.models.auth import UserExtensionist as UserExtensionistModel, UserProducter as UserProducterModel, ProductProperty as ProductPropertyModel
from modules.auth.infraestructure_auth.mappers.user_producter_mapper import UserProducterMapper
from modules.auth.infraestructure_auth.mappers.product_property_mapper import ProductPropertyMapper
from common.infrastructure.database.models.auth import ProductProperty

class PostgreSQLAuthRepository(AuthRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_email(self, email: str) -> Optional[UserExtensionist]:
        stmt = select(UserExtensionistModel).where(UserExtensionistModel.email == email)
        model = self.session.execute(stmt).scalar_one_or_none()
        return self._to_domain_entity(model) if model else None

    def get_user_by_identification(self, identification: str) -> Optional[UserExtensionist]:
        stmt = select(UserExtensionistModel).where(UserExtensionistModel.identification == identification)
        model = self.session.execute(stmt).scalar_one_or_none()
        return self._to_domain_entity(model) if model else None

    def get_user_by_token(self, token: str) -> Optional[UserExtensionist]:
        stmt = select(UserExtensionistModel).where(UserExtensionistModel.api_token == token)
        model = self.session.execute(stmt).scalar_one_or_none()
        return self._to_domain_entity(model) if model else None

    def get_user_by_api_key(self, api_key: str) -> Optional[UserExtensionist]:
        stmt = select(UserExtensionistModel).where(UserExtensionistModel.api_token == api_key)
        model = self.session.execute(stmt).scalar_one_or_none()
        return self._to_domain_entity(model) if model else None

    def save_producter(self, producter: UserProducter) -> UserProducter:
        producter_model = UserProducterMapper.to_db_model(producter)
        self.session.add(producter_model)
        self.session.commit()
        self.session.refresh(producter_model)
        return UserProducterMapper.to_entity(producter_model)

    def get_property_by_name(self, name: str) -> Optional[ProductProperty]:
        stmt = select(ProductPropertyModel).where(ProductPropertyModel.name == name)
        model = self.session.execute(stmt).scalar_one_or_none()
        return ProductPropertyMapper.to_entity(model) if model else None

    def save_property(self, property: ProductProperty) -> ProductProperty:
        property_model = ProductPropertyMapper.to_db_model(property)
        self.session.add(property_model)
        self.session.commit()
        self.session.refresh(property_model)
        return ProductPropertyMapper.to_entity(property_model)
        
    def save_extensionist(self, extensionist: UserExtensionist) -> UserExtensionist:
        extensionist_model = self._to_database_model(extensionist)
        self.session.add(extensionist_model)
        self.session.commit()
        self.session.refresh(extensionist_model)
        return self._to_domain_entity(extensionist_model)

    def _to_domain_entity(self, model: UserExtensionistModel) -> UserExtensionist:
        return UserExtensionist(
            id=model.id,
            name=model.name,
            email=model.email,
            phone=model.phone,
            type_id=model.type_id,
            identification=model.identification,
            city=model.city,
            zone=model.zone,
            signing_image_path=model.signing_image_path,
            api_token=model.api_token,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
            is_active=model.is_active,
        )

    def _to_database_model(self, entity: UserExtensionist) -> UserExtensionistModel:
        return UserExtensionistModel(
            id=entity.id,
            name=entity.name,
            email=entity.email,
            phone=entity.phone,
            type_id=entity.type_id,
            identification=entity.identification,
            city=entity.city,
            zone=entity.zone,
            signing_image_path=entity.signing_image_path,
            api_token=entity.api_token,
        )