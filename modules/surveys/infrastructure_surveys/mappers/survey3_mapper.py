from modules.surveys.domain_surveys.entities.survey3_entity import Survey3 as Survey3Entity
from common.infrastructure.database.models.survey import Survey3 as Survey3Model
from modules.surveys.infrastructure_surveys.mappers.user_producter_mapper import UserProducterMapper
from modules.surveys.infrastructure_surveys.mappers.product_property_mapper import ProductPropertyMapper
import json
from datetime import datetime

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

class Survey3Mapper:
    @staticmethod
    def to_db_model(survey_entity: Survey3Entity) -> Survey3Model:
        return Survey3Model(
            id=survey_entity.id if survey_entity.id != 0 else None,
            extensionist_id=survey_entity.extensionist_id,
            user_producter_id=survey_entity.user_producter_id,
            property_id=survey_entity.property_id,
            classification_user=json.dumps(survey_entity.classification_user, cls=CustomJsonEncoder) if survey_entity.classification_user else None,
            medition_focalization=json.dumps(survey_entity.medition_focalization, cls=CustomJsonEncoder) if survey_entity.medition_focalization else None,
            objetive_accompaniment=survey_entity.objetive_accompaniment,
            initial_diagnosis=survey_entity.initial_diagnosis,
            recommendations_commitments=survey_entity.recommendations_commitments,
            observations=survey_entity.observations,
            visit_date=str(survey_entity.visit_date) if survey_entity.visit_date else None,
            attended_by=survey_entity.attended_by,
            user=survey_entity.user,
            worker_up=survey_entity.worker_up,
            Household_size=survey_entity.Household_size,
            other=survey_entity.other,
            photo_user=survey_entity.photo_user,
            photo_interaction=survey_entity.photo_interaction,
            photo_panorama=survey_entity.photo_panorama,
            phono_extra_1=survey_entity.phono_extra_1,
            state=survey_entity.state
        )

    @staticmethod
    def to_entity(survey_model: Survey3Model) -> Survey3Entity:
        return Survey3Entity(
            id=survey_model.id,
            extensionist_id=survey_model.extensionist_id,
            user_producter_id=survey_model.user_producter_id,
            user_producter=UserProducterMapper.to_entity(survey_model.user_producter) if survey_model.user_producter else None,
            property_id=survey_model.property_id,
            property=ProductPropertyMapper.to_entity(survey_model.property) if survey_model.property else None,
            classification_user=json.loads(survey_model.classification_user) if survey_model.classification_user else None,
            medition_focalization=json.loads(survey_model.medition_focalization) if survey_model.medition_focalization else None,
            objetive_accompaniment=survey_model.objetive_accompaniment,
            initial_diagnosis=survey_model.initial_diagnosis,
            recommendations_commitments=survey_model.recommendations_commitments,
            observations=survey_model.observations,
            visit_date=survey_model.visit_date,
            attended_by=survey_model.attended_by,
            user=survey_model.user,
            worker_up=survey_model.worker_up,
            Household_size=survey_model.Household_size,
            other=survey_model.other,
            photo_user=survey_model.photo_user,
            photo_interaction=survey_model.photo_interaction,
            photo_panorama=survey_model.photo_panorama,
            phono_extra_1=survey_model.phono_extra_1,
            state=survey_model.state
        )