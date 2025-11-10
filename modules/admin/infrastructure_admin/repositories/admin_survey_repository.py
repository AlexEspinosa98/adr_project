from logging import Logger
from typing import List, Optional, Tuple

from sqlalchemy import text
from sqlalchemy.orm import Session
import json
from common.infrastructure.logging.config import get_logger
from common.infrastructure.repositories.postgresql import BasePostgreSQLRepository
from modules.admin.application_admin.dtos.output_dto.admin_survey_list_output_dto import (
    AdminSurveyListOutputDTO,
)
from modules.admin.domain_admin.repositories.admin_survey_repository import (
    AdminSurveyRepository as IAdminSurveyRepository,
)
from modules.surveys.application_surveys.dtos.output_dto.product_property_output_dto import ProductPropertyOutputDTO


_LOGGER: Logger = get_logger(__name__)


class PostgreSQLAdminSurveyRepository(
    IAdminSurveyRepository,
):
    def __init__(self, session: Session):
        self.session = session

    def find_admin_surveys_with_filters(
        self,
        city: Optional[str] = None,
        extensionist_identification: Optional[str] = None,
        extensionist_name: Optional[str] = None,
    ) -> List[AdminSurveyListOutputDTO]:
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
            s.user,
            s.household_size as "Household_size",
            s.other,
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
            s.user,
            s."Household_size" as "Household_size",
            s.other,
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
            s.user,
            s.household_size as "Household_size",
            s.other,
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
        if extensionist_identification:
            filters.append("extensionist_identification ILIKE :extensionist_identification")
            params["extensionist_identification"] = f"%{extensionist_identification}%"
        if extensionist_name:
            filters.append("extensionist_name ILIKE :extensionist_name")
            params["extensionist_name"] = f"%{extensionist_name}%"

        if filters:
            final_query = f"SELECT * FROM ({base_query}) as all_admin_surveys WHERE {" AND ".join(filters)}"
        else:
            final_query = f"SELECT * FROM ({base_query}) as all_admin_surveys"

        result = self.session.execute(text(final_query), params).fetchall()

        processed_results = []
        for row in result:
            survey_data = row._asdict()
            if survey_data.get("classification_user") and isinstance(survey_data["classification_user"], str):
                survey_data["classification_user"] = json.loads(survey_data["classification_user"])
            if survey_data.get("medition_focalization") and isinstance(survey_data["medition_focalization"], str):
                survey_data["medition_focalization"] = json.loads(survey_data["medition_focalization"])
            processed_results.append(AdminSurveyListOutputDTO.model_validate(survey_data))
        
        return processed_results

    def find_product_properties_by_extensionist_id(
        self, extensionist_id: int
    ) -> List[ProductPropertyOutputDTO]:
        _LOGGER.info(f"Finding unique product properties for extensionist ID: [{extensionist_id}]")

        query = """
        SELECT DISTINCT
            pp.id,
            pp.name,
            pp.cadastral_record,
            pp.latitude,
            pp.longitude,
            pp.municipality,
            pp.department,
            pp.city,
            pp.neighborhood,
            pp.address,
            pp.is_active,
            pp.created_at,
            pp.updated_at,
            pp.deleted_at
        FROM product_property pp
        JOIN survey_1 s1 ON pp.id = s1.property_id
        WHERE s1.extensionist_id = :extensionist_id
        UNION
        SELECT DISTINCT
            pp.id,
            pp.name,
            pp.cadastral_record,
            pp.latitude,
            pp.longitude,
            pp.municipality,
            pp.department,
            pp.city,
            pp.neighborhood,
            pp.address,
            pp.is_active,
            pp.created_at,
            pp.updated_at,
            pp.deleted_at
        FROM product_property pp
        JOIN survey_2 s2 ON pp.id = s2.property_id
        WHERE s2.extensionist_id = :extensionist_id
        UNION
        SELECT DISTINCT
            pp.id,
            pp.name,
            pp.cadastral_record,
            pp.latitude,
            pp.longitude,
            pp.municipality,
            pp.department,
            pp.city,
            pp.neighborhood,
            pp.address,
            pp.is_active,
            pp.created_at,
            pp.updated_at,
            pp.deleted_at
        FROM product_property pp
        JOIN survey_3 s3 ON pp.id = s3.property_id
        WHERE s3.extensionist_id = :extensionist_id
        """

        result = self.session.execute(text(query), {"extensionist_id": extensionist_id}).fetchall()

        return [ProductPropertyOutputDTO.model_validate(row._asdict()) for row in result]
