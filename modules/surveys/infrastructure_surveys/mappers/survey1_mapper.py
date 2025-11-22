from modules.surveys.domain_surveys.entities.survey1_entity import (
    Survey1 as Survey1Entity,
)
from common.infrastructure.database.models.survey import Survey1 as Survey1Model
import json
from datetime import datetime
from modules.surveys.infrastructure_surveys.mappers.product_property_mapper import (
    ProductPropertyMapper,
)
from modules.surveys.infrastructure_surveys.mappers.user_producter_mapper import (
    UserProducterMapper,
)


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


class Survey1Mapper:
    @staticmethod
    def to_db_model(survey_entity: Survey1Entity) -> Survey1Model:
        return Survey1Model(
            id=survey_entity.id if survey_entity.id != 0 else None,
            extensionist_id=survey_entity.extensionist_id,
            user_producter_id=survey_entity.user_producter_id,
            property_id=survey_entity.property_id,
            medition_focalization=survey_entity.medition_focalization,
            classification_user=survey_entity.classification_user,
            objetive_accompaniment=survey_entity.objetive_accompaniment,
            initial_diagnosis=survey_entity.initial_diagnosis,
            recommendations_commitments=survey_entity.recommendations_commitments,
            observations_visited=survey_entity.observations_visited,
            photo_user=survey_entity.photo_user,
            photo_interaction=survey_entity.photo_interaction,
            photo_panorama=survey_entity.photo_panorama,
            phono_extra_1=survey_entity.phono_extra_1,
            state=survey_entity.state,
            date_hour_end=survey_entity.date_hour_end,
            date_acompanamiento=survey_entity.date_acompanamiento,
            hour_acompanamiento=survey_entity.hour_acompanamiento,
            origen_register=survey_entity.origen_register,
            name_acompanamiento=survey_entity.name_acompanamiento,
            visit_date=survey_entity.visit_date,
            attended_by=survey_entity.attended_by,

        )

    @staticmethod
    def to_entity(survey_model: Survey1Model) -> Survey1Entity:
        def _parse_json(val):
            if isinstance(val, str):
                try:
                    return json.loads(val)
                except (json.JSONDecodeError, TypeError):
                    return val
            return val

        return Survey1Entity(
            id=survey_model.id,
            extensionist_id=survey_model.extensionist_id,
            user_producter_id=survey_model.user_producter_id,
            property_id=survey_model.property_id,
            user_producter=UserProducterMapper.to_entity(survey_model.user_producter)
            if survey_model.user_producter
            else None,
            property=ProductPropertyMapper.to_entity(survey_model.property)
            if survey_model.property
            else None,
            medition_focalization=_parse_json(survey_model.medition_focalization),
            classification_user=_parse_json(survey_model.classification_user),
            objetive_accompaniment=_parse_json(survey_model.objetive_accompaniment),
            initial_diagnosis=survey_model.initial_diagnosis,
            recommendations_commitments=survey_model.recommendations_commitments,
            observations_visited=survey_model.observations_visited,
            photo_user=survey_model.photo_user,
            photo_interaction=survey_model.photo_interaction,
            photo_panorama=survey_model.photo_panorama,
            phono_extra_1=survey_model.phono_extra_1,
            state=str.lower(survey_model.state),
            date_hour_end=survey_model.date_hour_end,
            date_acompanamiento=survey_model.date_acompanamiento,
            hour_acompanamiento=survey_model.hour_acompanamiento,
            origen_register=survey_model.origen_register,
            name_acompanamiento=survey_model.name_acompanamiento,
            visit_date=survey_model.visit_date,
            attended_by=survey_model.attended_by,
        )
