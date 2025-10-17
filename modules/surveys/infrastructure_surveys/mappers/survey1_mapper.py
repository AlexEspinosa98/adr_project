from modules.surveys.domain_surveys.entities.survey1_entity import Survey1 as Survey1Entity
from common.infrastructure.database.models.survey import Survey1 as Survey1Model

class Survey1Mapper:
    @staticmethod
    def to_db_model(survey_entity: Survey1Entity) -> Survey1Model:
        return Survey1Model(
            id=survey_entity.id if survey_entity.id != 0 else None,
            extensionist_id=survey_entity.extensionist_id,
            user_producter_id=survey_entity.user_producter_id,
            property_id=survey_entity.property_id,
            classification_user=survey_entity.classification_user,
            medition_focalization=survey_entity.medition_focalization,
            objetive_accompaniment=survey_entity.objetive_accompaniment,
            initial_diagnosis=survey_entity.initial_diagnosis,
            recommendations_commitments=survey_entity.recommendations_commitments,
            observations=survey_entity.observations,
            visit_date=survey_entity.visit_date,
            attended_by=survey_entity.attended_by,
            user=survey_entity.user,
            worker_up=survey_entity.worker_up,
            Household_size=survey_entity.Household_size,
            other=survey_entity.other,
            photo_user=survey_entity.photo_user,
            photo_interaction=survey_entity.photo_interaction,
            photo_panorama=survey_entity.photo_panorama,
            phono_extra_1=survey_entity.phono_extra_1
        )

    @staticmethod
    def to_entity(survey_model: Survey1Model) -> Survey1Entity:
        return Survey1Entity(
            id=survey_model.id,
            extensionist_id=survey_model.extensionist_id,
            user_producter_id=survey_model.user_producter_id,
            property_id=survey_model.property_id,
            classification_user=survey_model.classification_user,
            medition_focalization=survey_model.medition_focalization,
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
            phono_extra_1=survey_model.phono_extra_1
        )