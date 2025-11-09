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
  "observations": "Observations from the visit",
  "visit_date": "2025-11-07T10:00:00",
  "attended_by": "Name of the person attended",
  "user": "Associated user",
  "worker_up": "UP Worker",
  "Household_size": "4",
  "other": "Other relevant information",
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
  }
}
```

#### Example `producter_data` JSON:
```json
{
  "identification": "123456789",
  "name": "John Doe",
  "type_id": 1,
  "is_woman_rural": false,
  "is_young_rural": true,
  "ethnic_belonging": "None",
  "is_victim_conflict": false,
  "is_narp": false
}
```

#### Example `property_data` JSON:
```json
{
  "name": "La Esperanza Farm",
  "latitude": "11.23",
  "longitude": "-74.20",
  "asnm": "100",
  "total_area": "50",
  "state": "Magdalena",
  "city": "Santa Marta",
  "village": "Minca",
  "linea_productive_primary": "Coffee",
  "area_total_linea_productive_primary": "30",
  "linea_productive_secondary": "Avocado",
  "area_total_linea_productive_secondary": "10",
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
    "observations": "Observations",
    "visit_date": "2025-11-08T11:00:00",
    "attended_by": "Jane Doe",
    "user": "Associated user",
    "worker_up": "UP Worker",
    "Household_size": "3",
    "other": "Other info"
}
```

### Success Response

- **Status Code:** `201 CREATED`
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
  "medition_focalization": {},
  "objetive_accompaniment": "Final visit objective",
  "initial_diagnosis": "Final diagnosis",
  "recommendations_commitments": "Final recommendations",
  "observations": "Final observations",
  "visit_date": "2025-11-09T12:00:00",
  "attended_by": "John Smith",
  "user": "Associated user",
  "worker_up": "UP Worker",
  "Household_size": "5",
  "other": "Final notes",
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
        "type_id": 1,
        "identification": "123456789",
        "is_woman_rural": false,
        "is_young_rural": true,
        "ethnic_belonging": "None",
        "is_victim_conflict": false,
        "is_narp": false
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
        "total_area": "50",
        "linea_productive_primary": "Coffee",
        "area_total_linea_productive_primary": "30",
        "linea_productive_secondary": "Avocado",
        "area_total_linea_productive_secondary": "10",
        "area_in_production": "40"
    },
    "medition_focalization": {},
    "objetive_accompaniment": "Objective of the visit",
    "initial_diagnosis": "Initial diagnosis of the property",
    "recommendations_commitments": "Recommendations and commitments",
    "observations_visited": "Observations from the visit",
    "visit_date": "2025-11-07T10:00:00",
    "attended_by": "Name of the person attended",
    "user": "Associated user",
    "worker_up": "UP Worker",
    "Household_size": "4",
    "other": "Other relevant information",
    "photo_user": "./uploads/photo1.jpg",
    "photo_interaction": "./uploads/photo2.jpg",
    "photo_panorama": null,
    "phono_extra_1": null,
    "state": "PENDING"
  }
}
```
