from logging import Logger
from typing import List, Optional, Tuple

from sqlalchemy import Result, Select, select
from sqlalchemy.orm import Session

from common.infrastructure.database.models.auth import (
    UserExtensionist as UserExtensionistModel,
)
from common.infrastructure.logging.config import get_logger
from common.infrastructure.repositories.postgresql import BasePostgreSQLRepository
from modules.admin.domain_admin.entities.extensionist_user_entity import (
    ExtensionistUser,
)
from modules.admin.domain_admin.repositories.extensionist_user_repository import (
    ExtensionistUserRepository as IExtensionistUserRepository,
)

_LOGGER: Logger = get_logger(__name__)


class ExtensionistUserRepository(
    BasePostgreSQLRepository[ExtensionistUser, UserExtensionistModel],
    IExtensionistUserRepository,
):
    def __init__(self, session: Session) -> None:
        super().__init__(session, UserExtensionistModel)

    def find_all_with_filters(
        self,
        name: Optional[str] = None,
        identification: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        city: Optional[str] = None,
    ) -> List[ExtensionistUser]:
        stmt: Select[Tuple[UserExtensionistModel]] = select(UserExtensionistModel)

        if name:
            stmt = stmt.where(UserExtensionistModel.name.ilike(f"%{name}%"))
        if identification:
            stmt = stmt.where(
                UserExtensionistModel.identification.ilike(f"%{identification}%")
            )
        if email:
            stmt = stmt.where(UserExtensionistModel.email.ilike(f"%{email}%"))
        if phone:
            stmt = stmt.where(UserExtensionistModel.phone.ilike(f"%{phone}%"))
        if city:
            stmt = stmt.where(UserExtensionistModel.city.ilike(f"%{city}%"))

        result: Result[Tuple[UserExtensionistModel]] = self._session.execute(stmt)
        user_models = result.scalars().all()

        return [self._to_domain_entity(model) for model in user_models]

    def _to_domain_entity(self, model: UserExtensionistModel) -> ExtensionistUser:
        return ExtensionistUser(
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
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
        )

    def _to_database_model(self, entity: ExtensionistUser) -> UserExtensionistModel:
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
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            deleted_at=entity.deleted_at,
        )
