# API Endpoints for Surveys

This document provides detailed information about the API endpoints available in the `surveys` module.

---

## Create Survey 1

- **Method:** `POST`
- **Path:** `/surveys/1`
- **Description:** Creates a new Survey 1 record. This endpoint expects multipart/form-data, including survey data as JSON strings and uploaded files.

### Request

- **Headers:**
  - `Content-Type`: `multipart/form-data`

- **Form Data:**
  - `api_key` (string, required): The API key of the extensionist.
  - `survey_data` (string, required): A JSON string representing the `CreateSurvey1InputDTO`.
  - `producter_data` (string, required): A JSON string representing the `SurveyUserProducterInputDTO`.
  - `property_data` (string, required): A JSON string representing the `PropertyInfoInputDTO`.
  - `classification_user_data` (string, required): A JSON string representing the `ClassificationUserInputDTO`.
  - `files` (file, required): At least one file to be uploaded (e.g., `photo_user`, `photo_interaction`, `photo_panorama`).

#### Example `survey_data` JSON:
```json
{
  "medition_focalization": {
    "control_resources": {"obervation": "Notes on resource control",
    "score": 4},
    "voice_influence_decision": {"obervation": "Notes on voice influence decision",
    "score": 3},
    "leadership_innovation": {"obervation": "Notes on leadership innovation",
    "score": 5},
    "dialogue_knowledge": {"obervation": "Notes on dialogue knowledge",
    "score": 4}
  },
  "objetive_accompaniment": "Objective of the visit",
  "initial_diagnosis": "Initial diagnosis of the property",
  "recommendations_commitments": "Recommendations and commitments",
  "observations_visited": "Observations from the visit",
  "visit_date": "2025-11-07T10:00:00",
  "attended_by": "Name of the person attended",
  "classification_user": {
    "development_human_capacity": {"observation": "Notes on human capacity",
    "score": 3},
    "development_social_capacity": {"observation": "Notes on social capacity",
    "score": 2},
    "access_adaptative_adoption_information": {"observation": "Notes on productive capacity",
    "score": 4},
    "sustainable_management_natural_resources": {"observation": "Notes on financial capacity",
    "score": 3},
    "participation_public_political": {"observation": "Notes on political capacity",
    "score": 2}
  },
  "date_acompanamiento": "2025-11-07T10:00:00",
  "origen_register": "MOBILE",
  "name_acompanamiento": "pepito"
}
```

#### Example `producter_data` JSON:
```json
{
  "identification": "123456789",
  "name": "John Doe",
  "type_id": "CC",
  "number_phone": "3001234567",
  "is_woman_rural": false,
  "is_young_rural": true,
  "ethnic_belonging": "None",
  "is_victim_conflict": false,
  "is_narp": false,
  "is_producer_organization_member": true,
  "organization_name": "ASOPROCAFE",
  "representantive1_name": "Jane Doe"
}
```

#### Example `property_data` JSON:
```json
{
  "name": "La Esperanza Farm",
  "latitude": "11.23",
  "longitude": "-74.20",
  "asnm": "100",
  "state": "Magdalena",
  "city": "Santa Marta",
  "village": "Minca",
  "linea_productive_primary": "Coffee",
  "linea_productive_secondary": "Avocado",
  "area_in_production": "40"
}
```

#### Example `classification_user_data` JSON:
```json
{
    "main_productive_activity": 1,
    "secondary_productive_activities": 2,
    "tools_and_equipment": 3,
    "good_agricultural_practices": 1,
    "commercialization_structure": 2,
    "markets": 3,
    "added_value": 1,
    "records": 2,
    "labor_type": 3,
    "credit_and_banking": 1,
    "organization_membership": 2,
    "collective_activities": 3,
    "entrepreneurship_associativity": 1,
    "commercial_alliances": 2,
    "technical_support": 3,
    "quality_certifications": 1,
    "intellectual_property": 2,
    "access_information_sources": 3,
    "access_to_ict": 1,
    "use_of_ict_decision": 2,
    "ict_skills": 3,
    "knowledge_appropriation": 1,
    "environmental_practices": 2,
    "sustainable_practices": 3,
    "climate_change_adaptation": 1,
    "environmental_regulations": 2,
    "participation_mechanisms": 3,
    "participation_tools": 1,
    "political_social_control": 2,
    "community_self_management": 3
}
```

### Success Response

- **Status Code:** `201 CREATED`
- **Body:**
```json
{
  "status": "success",
  "message": "Survey 1 created successfully",
  "data": {
    "id": 1
  }
}
```

---

## Create Survey 2

- **Method:** `POST`
- **Path:** `/surveys/2`
- **Description:** Creates a new Survey 2 record. This endpoint expects multipart/form-data.

### Request

- **Headers:**
  - `Content-Type`: `multipart/form-data`

- **Form Data:**
  - `api_key` (string, required): The API key of the extensionist.
  - `survey_data` (string, required): A JSON string representing the `CreateSurvey2InputDTO`.
  - `producter_data` (string, required): A JSON string representing the `SurveyUserProducterInputDTO`.
  - `property_data` (string, required): A JSON string representing the `PropertyInfoInputDTO`.
  - `files` (file, required): Files to be uploaded.

#### Example `survey_data` JSON:
```json
{
    "objective_accompaniment": "Follow-up objective",
    "visit_development_follow_up_activities": "Activities for follow-up",
    "previous_visit_recommendations_fulfilled": true,
    "recommendations_commitments": "New recommendations",
    "observations_visited": "Observations from the visit",
    "objective": "Objective of the previous visit",
    "visit_followup": "Progress, difficulties, pending tasks",
    "fulfilled_previous_recommendations": true,
    "new_recommendations": "New recommendations based on follow-up",
    "observations_seg": "Follow-up observations",
    "register_coinnovation": "Co-innovation registration details",
    "local_practice_tool_technology_coinnovation_identified": true,
    "local_coinovation_or_technology_record": true,
    "name_innovation": "Drip Irrigation System",
    "description_innovation": "A locally adapted drip irrigation system.",
    "problem_solution_innovation": "Solves water scarcity during dry seasons.",
    "origin_and_developers": "Developed by local farmers.",
    "materials_and_resources": "Recycled plastic bottles, hoses.",
    "process_functioning": "Water is slowly released to the plant roots.",
    "potential_replication": "High potential for replication in the region.",
    "observations_extensionist": "The innovation is simple and effective.",
    "date_hour_end": "2025-11-08T12:00:00",
    "socilization_next_event": "Next event will be on...",
    "date_acompanamiento": "2025-11-08",
    "hour_acompanamiento": "11:00",
    "origen_register": "MOBILE",
    "name_acompanamiento": "Seguimiento 1",
    "visit_date": "2025-11-08T11:00:00",
    "attended_by": "Jane Doe"
}
```

### Success Response

- **Status Code:** `201-CREATED`
- **Body:**
```json
{
  "status": "success",
  "message": "Survey 2 created successfully",
  "data": {
    "id": 2
  }
}
```

---

## Create Survey 3

- **Method:** `POST`
- **Path:** `/surveys/3`
- **Description:** Creates a new Survey 3 record. This endpoint is similar to Survey 1 but for a different stage.

### Request

- **Headers:**
  - `Content-Type`: `multipart/form-data`

- **Form Data:**
  - `api_key` (string, required): The API key of the extensionist.
  - `survey_data` (string, required): A JSON string for `CreateSurvey3InputDTO`.
  - `producter_data` (string, required): A JSON string for `SurveyUserProducterInputDTO`.
  - `property_data` (string, required): A JSON string for `PropertyInfoInputDTO`.
  - `classification_user_data` (string, required): A JSON string for `ClassificationUserInputDTO`.
  - `files` (file, required): Files to be uploaded.

#### Example `survey_data` JSON:
```json
{
    "classification_user": {
        "development_human_capacity": {"observation": "Final notes on human capacity", "score": 4},
        "development_social_capacity": {"observation": "Final notes on social capacity", "score": 3},
        "access_adaptative_adoption_information": {"observation": "Final notes on productive capacity", "score": 5},
        "sustainable_management_natural_resources": {"observation": "Final notes on financial capacity", "score": 4},
        "participation_public_political": {"observation": "Final notes on political capacity", "score": 3}
    },
    "medition_focalization": {
        "control_resources": {"obervation": "Final notes on resource control", "score": 5},
        "voice_influence_decision": {"obervation": "Final notes on voice influence decision", "score": 4},
        "leadership_innovation": {"obervation": "Final notes on leadership innovation", "score": 5},
        "dialogue_knowledge": {"obervation": "Final notes on dialogue knowledge", "score": 4}
    },
    "objetive_accompaniment": "Final visit objective",
    "development_accompaniment": "Development of the final accompaniment.",
    "final_diagnosis": "Final diagnosis of the property.",
    "recommendations_commitments": "Final recommendations and commitments.",
    "observations_visited": "Final observations from the visit.",
    "date_hour_end": "2025-11-09T13:00:00",
    "socialization_events_group": "Socialization of results with the producer group.",
    "not_agend_new_visit": "No new visit is scheduled as this is the final one.",
    "date_acompanamiento": "2025-11-09",
    "hour_acompanamiento": "12:00",
    "origen_register": "WEB",
    "name_acompanamiento": "Diagnóstico Final",
    "visit_date": "2025-11-09T12:00:00",
    "attended_by": "John Smith",
    "state": "PENDING"
}
```

### Success Response

- **Status Code:** `201 CREATED`
- **Body:**
```json
{
  "status": "success",
  "message": "Survey 3 created successfully",
  "data": {
    "id": 3
  }
}
```

---

## Update Survey

- **Method:** `PUT`
- **Path:** `/surveys/{survey_type}/{survey_id}`
- **Description:** Updates an existing survey. This action is only permitted if the survey's current status is `rejected`. After a successful update, the survey's status is automatically set back to `pending` for re-evaluation.

### Request

- **Path Parameters:**
  - `survey_type` (integer, required): The type of survey to update (1, 2, or 3).
  - `survey_id` (integer, required): The ID of the survey to update.

- **Headers:**
  - `Content-Type`: `multipart/form-data`

- **Form Data:**
  - `api_key` (string, required): The API key of the extensionist.
  - `survey_data` (string, required): A JSON string representing the `UpdateSurveyXInputDTO` with the fields to be updated.
  - `files` (file, optional): Up to 4 new image files. If provided, they will replace the existing ones.

#### Example `survey_data` for Survey 1 (`/surveys/1/{survey_id}`):
Note: `classification_user` cannot be updated.
```json
{
  "objetive_accompaniment": "Corrected objective of the visit",
  "recommendations_commitments": "Updated recommendations and commitments after review."
}
```

#### Example `survey_data` for Survey 2 (`/surveys/2/{survey_id}`):
```json
{
  "recommendations_commitments": "Adjusted recommendations for co-innovation.",
  "observations_visited": "Additional observations noted during the follow-up."
}
```

#### Example `survey_data` for Survey 3 (`/surveys/3/{survey_id}`):
Note: `classification_user` cannot be updated.
```json
{
    "final_diagnosis": "Revised final diagnosis based on feedback.",
    "other": "Correction on final notes."
}
```

### Success Response

- **Status Code:** `200 OK`
- **Body:**
```json
{
  "status": "success",
  "message": "Survey 1 with ID 123 updated successfully and set to pending.",
  "data": {
    "id": 123,
    "state": "pending"
  }
}
```

### Error Responses

- **Status Code:** `403 FORBIDDEN`
  - **Condition:** The survey's current state is not `rejected`.
  - **Body:** 
    ```json
    {
      "detail": "Survey can only be edited if its state is 'rejected'. Current state is 'pending'."
    }
    ```
- **Status Code:** `404 NOT FOUND`
  - **Condition:** The survey with the given `survey_id` and `survey_type` does not exist.
  - **Body:** 
    ```json
    {
      "detail": "Survey not found"
    }
    ```

---

## List Surveys

- **Method:** `GET`
- **Path:** `/surveys`
- **Description:** Retrieves a paginated list of all surveys, with optional filters.

### Request

- **Query Parameters:**
  - `page` (integer, optional, default: 1): The page number to retrieve.
  - `limit` (integer, optional, default: 10): The number of items per page.
  - `sort_by` (string, optional, default: "id"): The field to sort by.
  - `sort_direction` (string, optional, default: "asc"): The sort direction (`asc` or `desc`).
  - `api_key` (string, optional): Filter by extensionist API key.
  - `start_date` (datetime, optional): Filter by visit date (start).
  - `end_date` (datetime, optional): Filter by visit date (end).
  - `farm_name` (string, optional): Filter by farm name (case-insensitive).
  - `survey_type` (integer, optional): Filter by survey type (1, 2, or 3).

### Success Response

- **Status Code:** `200 OK`
- **Body:**
```json
{
  "status": "success",
  "message": "Surveys retrieved successfully",
  "data": [
    {
      "id": 1,
      "survey_type": "Survey 1",
      "farm_name": "La Esperanza Farm",
      "visit_date": "2025-11-07T10:00:00",
      "state": "PENDING",
      "producter_name": "John Doe",
      "extensionist_name": "Alex Espinosa",
      "created_at": "2025-11-07T10:05:00"
    }
  ],
  "pagination": {
    "total_items": 1,
    "total_pages": 1,
    "current_page": 1,
    "limit": 10
  }
}
```

---

## Get Survey Detail

- **Method:** `GET`
- **Path:** `/surveys/{survey_type}/{survey_id}`
- **Description:** Retrieves the detailed information for a specific survey.

### Request

- **Path Parameters:**
  - `survey_type` (integer, required): The type of survey (1, 2, or 3).
  - `survey_id` (integer, required): The ID of the survey.

### Success Response (Example for Survey 1)

- **Status Code:** `200 OK`
- **Body:**
```json
{
  "status": "success",
  "message": "Survey type 1 with ID 1 retrieved successfully",
  "data": {
    "id": 1,
    "user_producter": {
        "id": 1,
        "name": "John Doe",
        "type_id": "CC",
        "identification": "123456789",
        "is_woman_rural": false,
        "is_young_rural": true,
        "ethnic_belonging": "None",
        "is_victim_conflict": false,
        "is_narp": false,
        "number_phone": "3001234567",
        "is_producer_organization_member": true,
        "organization_name": "ASOPROCAFE",
        "representantive1_name": "Jane Doe"
    },
    "property": {
        "id": 1,
        "name": "La Esperanza Farm",
        "latitude": "11.23",
        "longitude": "-74.20",
        "asnm": "100",
        "state": "Magdalena",
        "city": "Santa Marta",
        "village": "Minca",
        "linea_productive_primary": "Coffee",
        "linea_productive_secondary": "Avocado",
        "area_in_production": "40"
    },
    "medition_focalization": {},
    "objetive_accompaniment": "Objective of the visit",
    "initial_diagnosis": "Initial diagnosis of the property",
    "recommendations_commitments": "Recommendations and commitments",
    "observations_visited": "Observations from the visit",
    "visit_date": "2025-11-07T10:00:00",
    "attended_by": "Name of the person attended",
    "photo_user": "./uploads/photo1.jpg",
    "photo_interaction": "./uploads/photo2.jpg",
    "photo_panorama": null,
    "phono_extra_1": null,
    "state": "PENDING"
  }
}
```
