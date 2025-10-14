from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from common.infrastructure.database.models.auth import UserExtensionist as UserExtensionistModel
from common.infrastructure.repositories.postgresql.base_repository import BasePostgreSQLRepository

class PostgreSQLAuthRepository(BasePostgreSQLRepository[UserExtensionist, UserExtensionistModel], AuthRepository):
    def __init__(self, session: Session):
        super().__init__(session, UserExtensionistModel)

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

    def get_user_by_email(self, email: str) -> Optional[UserExtensionist]:
        stmt = select(self._model_class).where(self._model_class.email == email)
        model = self._session.execute(stmt).scalar_one_or_none()
        return self._to_domain_entity(model) if model else None

    def get_user_by_identification(self, identification: str) -> Optional[UserExtensionist]:
        stmt = select(self._model_class).where(self._model_class.identification == identification)
        model = self._session.execute(stmt).scalar_one_or_none()
        return self._to_domain_entity(model) if model else None

    def get_user_by_token(self, token: str) -> Optional[UserExtensionist]:
        stmt = select(self._model_class).where(self._model_class.api_token == token)
        model = self._session.execute(stmt).scalar_one_or_none()
        return self._to_domain_entity(model) if model else None
