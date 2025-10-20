from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Optional, Tuple
from datetime import datetime
from modules.surveys.application_surveys.dtos.output_dto.survey_list_item_dto import SurveyListItemDTO
from modules.surveys.domain_surveys.repositories.list_surveys_repository import ListSurveysRepository
from common.application.dtos.input_dto.pagination_dto import PaginationInputDTO

class PostgreSQLListSurveysRepository(ListSurveysRepository):
    def __init__(self, session: Session):
        self.session = session

    def list_surveys(
        self,
        pagination: PaginationInputDTO,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        farm_name: Optional[str] = None,
        survey_type: Optional[int] = None,
    ) -> Tuple[list[SurveyListItemDTO], int]:
        
        base_query = """
        (SELECT s.id, 'Survey 1' as survey_type, pp.name as farm_name, s.visit_date, s.state, up.name as producter_name, ue.name as extensionist_name
        FROM survey_1 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.user_producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id)
        UNION ALL
        (SELECT s.id, 'Survey 2' as survey_type, pp.name as farm_name, s.visit_date, s.state, up.name as producter_name, ue.name as extensionist_name
        FROM survey_2 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id)
        UNION ALL
        (SELECT s.id, 'Survey 3' as survey_type, pp.name as farm_name, s.visit_date, s.state, up.name as producter_name, ue.name as extensionist_name
        FROM survey_3 s
        LEFT JOIN product_property pp ON s.property_id = pp.id
        LEFT JOIN user_producter up ON s.user_producter_id = up.id
        LEFT JOIN user_extensionist ue ON s.extensionist_id = ue.id)
        """

        filters = []
        params = {}

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
            filters.append(f"survey_type = 'Survey {survey_type}'")

        if filters:
            base_query = f"SELECT * FROM ({base_query}) as all_surveys WHERE {" AND ".join(filters)}"
        else:
            base_query = f"SELECT * FROM ({base_query}) as all_surveys"

        count_query = f"SELECT COUNT(*) FROM ({base_query}) as count_query"
        total_items = self.session.execute(text(count_query), params).scalar_one()

        base_query += f" ORDER BY {pagination.sort_by} {pagination.sort_direction.value} LIMIT :limit OFFSET :offset"
        params["limit"] = pagination.limit
        params["offset"] = pagination.offset

        result = self.session.execute(text(base_query), params).fetchall()

        return [SurveyListItemDTO.model_validate(row, from_attributes=True) for row in result], total_items
