# API Endpoint JSON Examples

## @modules/auth

### POST /auth/register_extensionist

**Input DTO: `UserExtensionistInputDTO`**

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "type_id": "cc",
  "identification": "123456789",
  "city": "Sample City",
  "zone": "Sample Zone",
  "phone": "123-456-7890"
}
```

### POST /auth/user/signing-image

**Input:** `UploadFile` (file upload) and `api_token` (query parameter)

Example usage (using `curl`):
```bash
curl -X POST "http://localhost:8000/auth/user/signing-image?api_token=YOUR_API_TOKEN" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/image.png;type=image/png"
```

### PUT /auth/register_extensionist

**Input DTO: `UpdateUserExtensionistBodyDTO`**

```json
{
  "name": "Jane Doe",
  "phone": "987-654-3210",
  "city": "New City"
}
```

## @modules/surveys

### POST /surveys/1

**Input:** `api_key` (Form), `survey_data` (Form, JSON string of `CreateSurvey1InputDTO`), `producter_data` (Form, JSON string of `SurveyUserProducterInputDTO`), `property_data` (Form, JSON string of `PropertyInfoInputDTO`), `classification_user_data` (Form, JSON string of `ClassificationUserInputDTO`), `files` (List of `UploadFile`)

**Example `producter_data` (JSON for `SurveyUserProducterInputDTO`):**

```json
{
  "identification": "PROD123",
  "name": "Producer One",
  "type_id": 1,
  "is_woman_rural": true,
  "is_young_rural": false,
  "ethnic_belonging": "Indigenous",
  "is_victim_conflict": false,
  "is_narp": false
}
```

**Example `property_data` (JSON for `PropertyInfoInputDTO`):**

```json
{
  "name": "Farm A",
  "latitude": "10.123",
  "longitude": "-74.456",
  "asnm": "ASNM123",
  "total_area": "100ha",
  "state": "Magdalena",
  "city": "Santa Marta",
  "village": "Minca",
  "area_total_property": "100",
  "linea_productive_primary": "Coffee",
  "area_total_linea_productive_primary": "50",
  "linea_productive_secondary": "Cacao",
  "area_total_linea_productive_secondary": "20",
  "area_in_production": "70"
}
```

**Example `classification_user_data` (JSON for `ClassificationUserInputDTO`):**

```json
{
  "main_productive_activity": 1,
  "secondary_productive_activities": 2,
  "tools_and_equipment": 3,
  "good_agricultural_practices": 4,
  "commercialization_structure": 5,
  "markets": 6,
  "added_value": 7,
  "records": 8,
  "labor_type": 9,
  "credit_and_banking": 10,
  "organization_membership": 1,
  "collective_activities": 2,
  "entrepreneurship_associativity": 3,
  "commercial_alliances": 4,
  "technical_support": 5,
  "quality_certifications": 6,
  "intellectual_property": 7,
  "access_information_sources": 8,
  "access_to_ict": 9,
  "use_of_ict_decision": 10,
  "ict_skills": 1,
  "knowledge_appropriation": 2,
  "environmental_practices": 3,
  "sustainable_practices": 4,
  "climate_change_adaptation": 5,
  "environmental_regulations": 6,
  "participation_mechanisms": 7,
  "participation_tools": 8,
  "political_social_control": 9,
  "community_self_management": 10
}
```

**Example `survey_data` (JSON for `CreateSurvey1InputDTO`):**

```json
{
  "medition_focalization": {
    "focus": "Water",
    "level": "High"
  },
  "objetive_accompaniment": "Improve water management",
  "initial_diagnosis": "Lack of irrigation system",
  "recommendations_commitments": "Install drip irrigation",
  "observations": "Producer is very cooperative",
  "visit_date": "2025-10-27T10:00:00Z",
  "attended_by": "Extensionist Name",
  "state": "PENDING"
}
```

**Example `curl` request for POST /surveys/1:**
```bash
curl -X POST "http://localhost:8000/surveys/1" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "api_key=YOUR_API_KEY" \
  -F "survey_data={ \"medition_focalization\": { \"focus\": \"Water\", \"level\": \"High\" }, \"objetive_accompaniment\": \"Improve water management\", \"initial_diagnosis\": \"Lack of irrigation system\", \"recommendations_commitments\": \"Install drip irrigation\", \"observations\": \"Producer is very cooperative\", \"visit_date\": \"2025-10-27T10:00:00Z\", \"attended_by\": \"Extensionist Name\", \"state\": \"PENDING\" }" \
  -F "producter_data={ \"identification\": \"PROD123\", \"name\": \"Producer One\", \"type_id\": 1, \"is_woman_rural\": true, \"is_young_rural\": false, \"ethnic_belonging\": \"Indigenous\", \"is_victim_conflict\", false, \"is_narp\": false }" \
  -F "property_data={ \"name\": \"Farm A\", \"latitude\": \"10.123\", \"longitude\": \"-74.456\", \"asnm\": \"ASNM123\", \"total_area\": \"100ha\", \"state\": \"Magdalena\", \"city\": \"Santa Marta\", \"village\": \"Minca\", \"area_total_property\": \"100\", \"linea_productive_primary\": \"Coffee\", \"area_total_linea_productive_primary\": \"50\", \"linea_productive_secondary\": \"Cacao\", \"area_total_linea_productive_secondary\": \"20\", \"area_in_production\": \"70\" }" \
  -F "classification_user_data={ \"main_productive_activity\": 1, \"secondary_productive_activities\": 2, \"tools_and_equipment\": 3, \"good_agricultural_practices\": 4, \"commercialization_structure\": 5, \"markets\": 6, \"added_value\": 7, \"records\": 8, \"labor_type\": 9, \"credit_and_banking\": 10, \"organization_membership\": 1, \"collective_activities\": 2, \"entrepreneurship_associativity\": 3, \"commercial_alliances\": 4, \"technical_support\": 5, \"quality_certifications\": 6, \"intellectual_property\": 7, \"access_information_sources\": 8, \"access_to_ict\": 9, \"use_of_ict_decision\": 10, \"ict_skills\": 1, \"knowledge_appropriation\": 2, \"environmental_practices\": 3, \"sustainable_practices\": 4, \"climate_change_adaptation\": 5, \"environmental_regulations\": 6, \"participation_mechanisms\": 7, \"participation_tools\": 8, \"political_social_control\": 9, \"community_self_management\": 10 }" \
  -F "files=@/path/to/your/image1.png;type=image/png" \
  -F "files=@/path/to/your/image2.png;type=image/png"
```

### POST /surveys/3

**Input:** `api_key` (Form), `survey_data` (Form, JSON string of `CreateSurvey3InputDTO`), `producter_input_dto` (Body, JSON of `SurveyUserProducterInputDTO`), `property_info_input_dto` (Body, JSON of `PropertyInfoInputDTO`), `files` (List of `UploadFile`)

**Example `producter_input_dto` (JSON for `SurveyUserProducterInputDTO`):**

```json
{
  "identification": "PROD123",
  "name": "Producer One",
  "type_id": 1,
  "is_woman_rural": true,
  "is_young_rural": false,
  "ethnic_belonging": "Indigenous",
  "is_victim_conflict": false,
  "is_narp": false
}
```

**Example `property_info_input_dto` (JSON for `PropertyInfoInputDTO`):**

```json
{
  "name": "Farm A",
  "latitude": "10.123",
  "longitude": "-74.456",
  "asnm": "ASNM123",
  "total_area": "100ha",
  "state": "Magdalena",
  "city": "Santa Marta",
  "village": "Minca",
  "area_total_property": "100",
  "linea_productive_primary": "Coffee",
  "area_total_linea_productive_primary": "50",
  "linea_productive_secondary": "Cacao",
  "area_total_linea_productive_secondary": "20",
  "area_in_production": "70"
}
```

**Example `survey_data` (JSON for `CreateSurvey3InputDTO`):**

```json
{
  "classification_user": {
    "category": "B",
    "score": 15
  },
  "medition_focalization": {
    "focus": "Soil",
    "level": "Medium"
  },
  "objetive_accompaniment": "Improve soil fertility",
  "initial_diagnosis": "Low organic matter",
  "recommendations_commitments": "Apply compost",
  "observations": "Soil samples taken",
  "visit_date": "2025-10-28T11:00:00Z",
  "attended_by": "Extensionist Name 2",
  "state": "PENDING"
}
```

**Example `curl` request for POST /surveys/3:**
```bash
curl -X POST "http://localhost:8000/surveys/3" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "api_key=YOUR_API_KEY" \
  -F "survey_data={ \"classification_user\": { \"category\": \"B\", \"score\": 15 }, \"medition_focalization\": { \"focus\": \"Soil\", \"level\": \"Medium\" }, \"objetive_accompaniment\": \"Improve soil fertility\", \"initial_diagnosis\": \"Low organic matter\", \"recommendations_commitments\": \"Apply compost\", \"observations\": \"Soil samples taken\", \"visit_date\": \"2025-10-28T11:00:00Z\", \"attended_by\": \"Extensionist Name 2\", \"state\": \"PENDING\" }" \
  -F "files=@/path/to/your/image1.png;type=image/png" \
  -F "files=@/path/to/your/image2.png;type=image/png" \
  -F "producter_input_dto=@-" \
  -F "property_info_input_dto=@-" \
  --data-binary '{
    "producter_input_dto": {
      "identification": "PROD123",
      "name": "Producer One",
      "type_id": 1,
      "is_woman_rural": true,
      "is_young_rural": false,
      "ethnic_belonging": "Indigenous",
      "is_victim_conflict": false,
      "is_narp": false
    },
    "property_info_input_dto": {
      "name": "Farm A",
      "latitude": "10.123",
      "longitude": "-74.456",
      "asnm": "ASNM123",
      "total_area": "100ha",
      "state": "Magdalena",
      "city": "Santa Marta",
      "village": "Minca",
      "area_total_property": "100",
      "linea_productive_primary": "Coffee",
      "area_total_linea_productive_primary": "50",
      "linea_productive_secondary": "Cacao",
      "area_total_linea_productive_secondary": "20",
      "area_in_production": "70"
    }
  }'
```
