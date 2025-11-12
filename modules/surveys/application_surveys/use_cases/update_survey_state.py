from sqlalchemy.orm import Session
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey1_repository import (
    PostgreSQLSurvey1Repository,
)
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey2_repository import (
    PostgreSQLSurvey2Repository,
)
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey3_repository import (
    PostgreSQLSurvey3Repository,
)
from modules.admin.application_admin.use_cases.log_admin_action import LogAdminAction


class UpdateSurveyState:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.survey_repositories = {
            1: PostgreSQLSurvey1Repository(db_session),
            2: PostgreSQLSurvey2Repository(db_session),
            3: PostgreSQLSurvey3Repository(db_session),
        }
        self.log_admin_action = LogAdminAction(db_session)

    def execute(
        self, survey_type: int, survey_id: int, new_state: str, admin_user_id: int
    ):
        if survey_type not in self.survey_repositories:
            raise ValueError("Invalid survey type")

        repository = self.survey_repositories[survey_type]
        survey = repository.get_by_id(survey_id)

        if not survey:
            raise ValueError("Survey not found")

        old_state = survey.state
        survey.state = new_state

        # The save method in the survey repositories commits the session.
        # This is not ideal for a use case that does multiple things.
        # I will assume for now that this is the intended behavior of the application.
        updated_survey = repository.save(survey)

        # Log the action
        self.log_admin_action.execute(
            admin_user_id=admin_user_id,
            action_id=2,  # 'Aprobar/Rechazar Encuesta'
            description=f"Survey {survey_type} with ID {survey_id} state changed from {old_state} to {new_state}",
        )

        return updated_survey
