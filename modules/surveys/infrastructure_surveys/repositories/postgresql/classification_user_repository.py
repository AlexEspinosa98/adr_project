from sqlalchemy.orm import Session

from modules.surveys.domain_surveys.entities.classification_user_entity import ClassificationUser
from modules.surveys.domain_surveys.repositories.classification_user_repository import ClassificationUserRepository
from common.infrastructure.database.models.survey import ClassificationUser as ClassificationUserModel

class PostgreSQLClassificationUserRepository(ClassificationUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, classification_user: ClassificationUser) -> ClassificationUser:
        classification_user_model = ClassificationUserModel(**classification_user.dict())
        self.session.add(classification_user_model)
        self.session.commit()
        self.session.refresh(classification_user_model)
        return ClassificationUser(**classification_user_model.__dict__)
