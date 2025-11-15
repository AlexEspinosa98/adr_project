from sqlalchemy.orm import Session
from fastapi import Depends
from common.infrastructure.database.session import session_manager
from modules.surveys.application_surveys.services.update_survey_service import (
    UpdateSurveyService,
)
from modules.surveys.application_surveys.use_cases.update_survey_use_case import (
    UpdateSurveyUseCase,
)
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey1_repository import (
    PostgreSQLSurvey1Repository,
)
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey2_repository import (
    PostgreSQLSurvey2Repository,
)
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey3_repository import (
    PostgreSQLSurvey3Repository,
)


def get_update_survey_service(
    session: Session = Depends(session_manager.get_session),
) -> UpdateSurveyService:
    survey1_repo = PostgreSQLSurvey1Repository(session)
    survey2_repo = PostgreSQLSurvey2Repository(session)
    survey3_repo = PostgreSQLSurvey3Repository(session)

    update_survey_use_case = UpdateSurveyUseCase(
        survey1_repository=survey1_repo,
        survey2_repository=survey2_repo,
        survey3_repository=survey3_repo,
    )

    return UpdateSurveyService(update_survey_use_case=update_survey_use_case)
