from sqlalchemy.orm import Session
from common.domain.enums.survey_status import SurveyStatus
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
from modules.surveys.infrastructure_surveys.repositories.postgresql.survey_rejection_repository import PostgreSQLSurveyRejectionRepository
from modules.surveys.domain_surveys.entities.survey_rejection_entity import SurveyRejection


class UpdateSurveyState:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.survey_repositories = {
            1: PostgreSQLSurvey1Repository(db_session),
            2: PostgreSQLSurvey2Repository(db_session),
            3: PostgreSQLSurvey3Repository(db_session),
        }
        self.log_admin_action = LogAdminAction(db_session)
        self.survey_rejection_repository = PostgreSQLSurveyRejectionRepository(db_session)

    def execute(
        self, survey_type: int, survey_id: int, new_state: str, admin_user_id: int, rejection_reason: str | None = None
    ):
        if survey_type not in self.survey_repositories:
            raise ValueError("Invalid survey type")

        repository = self.survey_repositories[survey_type]
        survey = repository.get_by_id(survey_id)

        if not survey:
            raise ValueError("Survey not found")

        old_state_value = (
            survey.state.value if isinstance(survey.state, SurveyStatus) else survey.state
        )

        try:
            survey.state = SurveyStatus(new_state.lower())
        except ValueError:
            valid_states = ", ".join([s.value for s in SurveyStatus])
            raise ValueError(
                f"Invalid state: '{new_state}'. Must be one of {valid_states}"
            )

        updated_survey = repository.save(survey)

        if new_state.lower() == "rejected" and rejection_reason:
            rejection = SurveyRejection(
                id=None,
                survey_id=survey_id,
                survey_type=survey_type,
                reason=rejection_reason,
                admin_user_id=admin_user_id,
            )
            self.survey_rejection_repository.save(rejection)

        # Log the action
        self.log_admin_action.execute(
            admin_user_id=admin_user_id,
            action_id=2,  # 'Aprobar/Rechazar Encuesta'
            description=f"Survey {survey_type} with ID {survey_id} state changed from {old_state_value} to {new_state}",
        )

        return updated_survey
