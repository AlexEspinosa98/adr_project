from modules.surveys.domain_surveys.entities.survey1_entity import Survey1 as Survey1Entity
from common.infrastructure.database.models.survey import Survey1 as Survey1Model
import json
from datetime import datetime
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import ProductProperty

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
            
            medition_focalization=json.dumps(survey_entity.medition_focalization, cls=CustomJsonEncoder) if survey_entity.medition_focalization else None,
            objetive_accompaniment=survey_entity.objetive_accompaniment,
            initial_diagnosis=survey_entity.initial_diagnosis,
            recommendations_commitments=survey_entity.recommendations_commitments,
            observations_visited=survey_entity.observations_visited,
            visit_date=str(survey_entity.visit_date),
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
    def to_entity(survey_model: Survey1Model) -> Survey1Entity:
        return Survey1Entity(
            id=survey_model.id,
            extensionist_id=survey_model.extensionist_id,
            user_producter_id=survey_model.user_producter_id,
            user_producter=UserProducter(**survey_model.user_producter.__dict__) if survey_model.user_producter else None,
            property_id=survey_model.property_id,
            property=ProductProperty(**survey_model.property.__dict__) if survey_model.property else None,
            
            medition_focalization=json.loads(survey_model.medition_focalization) if survey_model.medition_focalization else None,
            objetive_accompaniment=survey_model.objetive_accompaniment,
            initial_diagnosis=survey_model.initial_diagnosis,
            recommendations_commitments=survey_model.recommendations_commitments,
            observations_visited=survey_model.observations_visited,
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
