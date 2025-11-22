from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Optional, Tuple, List
from datetime import datetime
from modules.surveys.application_surveys.dtos.output_dto.survey_list_item_dto import (
    SurveyListItemDTO,
)
from modules.surveys.domain_surveys.repositories.list_surveys_repository import (
    ListSurveysRepository,
)
from common.application.dtos.input_dto.pagination_dto import PaginationInputDTO
from modules.surveys.domain_surveys.entities.survey_entity import Survey
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter


class PostgreSQLListSurveysRepository(ListSurveysRepository):
    def __init__(self, session: Session):
        self.session = session

    def list_surveys(
        self,
        pagination: PaginationInputDTO,
        api_key: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        farm_name: Optional[str] = None,
        survey_type: Optional[int] = None,
        status: Optional[int] = None,
    ) -> Tuple[list[SurveyListItemDTO], int]:
        base_query = """
        (SELECT s.id, 1 as survey_type, pp.name as farm_name, s.visit_date, s.state, up.name as producter_name, ue.name as extensionist_name, ue.api_token, s.created_at, sr.reason as rejection_reason
        FROM survey_1 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.user_producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id
        LEFT JOIN survey_rejection sr ON s.id = sr.survey_id AND sr.survey_type = 1)
        UNION ALL
        (SELECT s.id, 2 as survey_type, pp.name as farm_name, s.visit_date, s.state, up.name as producter_name, ue.name as extensionist_name, ue.api_token, s.created_at, sr.reason as rejection_reason
        FROM survey_2 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id
        LEFT JOIN survey_rejection sr ON s.id = sr.survey_id AND sr.survey_type = 2)
        UNION ALL
        (SELECT s.id, 3 as survey_type, pp.name as farm_name, s.visit_date, s.state, up.name as producter_name, ue.name as extensionist_name, ue.api_token, s.created_at, sr.reason as rejection_reason
        FROM survey_3 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.user_producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id
        LEFT JOIN survey_rejection sr ON s.id = sr.survey_id AND sr.survey_type = 3)
        """

        filters = []
        params = {}

        if api_key:  # Changed
            filters.append("api_token = :api_key")
            params["api_key"] = api_key

        if start_date:
            filters.append("visit_date >= :start_date")
            params["start_date"] = start_date
        if end_date:
            filters.append("visit_date <= :end_date")
            params["end_date"] = end_date
        if farm_name:
            filters.append("farm_name ILIKE :farm_name")
            params["farm_name"] = f"%{farm_name}%"
        if survey_type:
            filters.append(f"survey_type = {survey_type}")
        if status is not None:            
            filters.append("state = :state")
            params["state"] = status

        if filters:
            base_query = f"SELECT * FROM ({base_query}) as all_surveys WHERE {' AND '.join(filters)}"
        else:
            base_query = f"SELECT * FROM ({base_query}) as all_surveys"

        count_query = f"SELECT COUNT(*) FROM ({base_query}) as count_query"
        total_items = self.session.execute(text(count_query), params).scalar_one()

        base_query += f" ORDER BY {pagination.sort_by} {pagination.sort_direction.value} LIMIT :limit OFFSET :offset"
        params["limit"] = pagination.limit
        params["offset"] = pagination.offset

        result = self.session.execute(text(base_query), params).fetchall()

        return [
            SurveyListItemDTO.model_validate(row, from_attributes=True)
            for row in result
        ], total_items

    def find_admin_surveys_with_filters(
        self, city: Optional[str] = None, extensionist: Optional[str] = None
    ) -> List[Survey]:
        base_query = """
        SELECT
            s.id,
            'Survey 1' as survey_type,
            s.extensionist_id,
            s.user_producter_id,
            s.property_id,
            s.objetive_accompaniment,
            NULL as initial_diagnosis,
            s.recommendations_commitments,
            s.observations_visited as observations,
            s.visit_date,
            s.attended_by,
            s.photo_user,
            s.photo_interaction,
            s.photo_panorama,
            s.phono_extra_1,
            s.state,
            s.classification_user::jsonb as classification_user,
            s.medition_focalization::jsonb as medition_focalization,
            pp.city as property_city,
            pp.name as property_name,
            up.name as user_producter_name,
            ue.name as extensionist_name,
            ue.identification as extensionist_identification
        FROM survey_1 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.user_producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id
        UNION ALL
        SELECT
            s.id,
            'Survey 2' as survey_type,
            s.extensionist_id,
            s.producter_id as user_producter_id, -- Map producter_id to user_producter_id for consistency
            s.property_id,
            s.objective_accompaniment,
            NULL as initial_diagnosis, -- Survey2 does not have initial_diagnosis
            s.recommendations_commitments,
            s.observations_visited as observations,
            s.visit_date,
            s.attended_by,
            s.photo_user,
            s.photo_interaction,
            s.photo_panorama,
            s.phono_extra_1,
            s.state,
            NULL as classification_user, -- Survey2 does not have classification_user
            NULL as medition_focalization, -- Survey2 does not have medition_focalization
            pp.city as property_city,
            pp.name as property_name,
            up.name as user_producter_name,
            ue.name as extensionist_name,
            ue.identification as extensionist_identification
        FROM survey_2 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id
        UNION ALL
        SELECT
            s.id,
            'Survey 3' as survey_type,
            s.extensionist_id,
            s.user_producter_id,
            s.property_id,
            s.objetive_accompaniment,
            NULL as initial_diagnosis,
            s.recommendations_commitments,
            s.observations_visited as observations,
            s.visit_date,
            s.attended_by,
            s.photo_user,
            s.photo_interaction,
            s.photo_panorama,
            s.phono_extra_1,
            s.state,
            s.classification_user::jsonb as classification_user,
            s.medition_focalization::jsonb as medition_focalization,
            pp.city as property_city,
            pp.name as property_name,
            up.name as user_producter_name,
            ue.name as extensionist_name,
            ue.identification as extensionist_identification
        FROM survey_3 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.user_producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id
        """

        filters = []
        params = {}

        if city:
            filters.append("property_city ILIKE :city")
            params["city"] = f"%{city}%"
        if extensionist:
            filters.append("extensionist_identification ILIKE :extensionist")
            params["extensionist"] = f"%{extensionist}%"

        if filters:
            final_query = f"SELECT * FROM ({base_query}) as all_admin_surveys WHERE {' AND '.join(filters)}"
        else:
            final_query = f"SELECT * FROM ({base_query}) as all_admin_surveys"

        result = self.session.execute(text(final_query), params).fetchall()

        # Manually map the results to the Survey entity
        surveys = []
        for row in result:
            survey_data = row._asdict()
            # Extract and create ProductProperty and UserProducter entities if data exists
            product_property = None
            if survey_data.get("property_id"):
                product_property = ProductProperty(
                    id=survey_data["property_id"],
                    city=survey_data.get("property_city"),
                    name=survey_data.get("property_name"),
                    # ... other ProductProperty fields if needed
                )

            user_producter = None
            if survey_data.get("user_producter_id"):
                user_producter = UserProducter(
                    id=survey_data["user_producter_id"],
                    name=survey_data.get("user_producter_name"),
                    # ... other UserProducter fields if needed
                )

            # Create Survey entity, handling fields that might be NULL from UNION ALL
            surveys.append(
                Survey(
                    id=survey_data["id"],
                    survey_type=survey_data["survey_type"],
                    extensionist_id=survey_data["extensionist_id"],
                    user_producter_id=survey_data["user_producter_id"],
                    user_producter=user_producter,
                    property_id=survey_data["property_id"],
                    property=product_property,
                    objetive_accompaniment=survey_data.get("objetive_accompaniment"),
                    initial_diagnosis=survey_data.get("initial_diagnosis"),
                    recommendations_commitments=survey_data.get(
                        "recommendations_commitments"
                    ),
                    observations=survey_data.get("observations"),
                    visit_date=survey_data.get("visit_date"),
                    attended_by=survey_data.get("attended_by"),
                    photo_user=survey_data.get("photo_user"),
                    photo_interaction=survey_data.get("photo_interaction"),
                    photo_panorama=survey_data.get("photo_panorama"),
                    phono_extra_1=survey_data.get("phono_extra_1"),
                    state=survey_data.get("state"),
                    classification_user=survey_data.get("classification_user"),
                    medition_focalization=survey_data.get("medition_focalization"),
                    # Survey2 specific fields
                    visit_development_follow_up_activities=survey_data.get(
                        "visit_development_follow_up_activities"
                    ),
                    previous_visit_recommendations_fulfilled=survey_data.get(
                        "previous_visit_recommendations_fulfilled"
                    ),
                    objective=survey_data.get("objective"),
                    visit_followup=survey_data.get("visit_followup"),
                    fulfilled_previous_recommendations=survey_data.get(
                        "fulfilled_previous_recommendations"
                    ),
                    new_recommendations=survey_data.get("new_recommendations"),
                    observations_seg=survey_data.get("observations_seg"),
                    register_coinnovation=survey_data.get("register_coinnovation"),
                    local_practice_tool_technology_coinnovation_identified=survey_data.get(
                        "local_practice_tool_technology_coinnovation_identified"
                    ),
                    local_coinovation_or_technology_record=survey_data.get(
                        "local_coinovation_or_technology_record"
                    ),
                    name_innovation=survey_data.get("name_innovation"),
                    description_innovation=survey_data.get("description_innovation"),
                    problem_solution_innovation=survey_data.get(
                        "problem_solution_innovation"
                    ),
                    origin_and_developers=survey_data.get("origin_and_developers"),
                    materials_and_resources=survey_data.get("materials_and_resources"),
                    process_functioning=survey_data.get("process_functioning"),
                    potential_replication=survey_data.get("potential_replication"),
                    observations_extensionist=survey_data.get(
                        "observations_extensionist"
                    ),
                    date_hour_end=survey_data.get("date_hour_end"),
                    socilization_next_event=survey_data.get("socilization_next_event"),
                )
            )
        return surveys
