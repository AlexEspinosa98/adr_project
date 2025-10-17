## JSON Examples for POST /surveys/1

### Example `producter_data` (JSON for `SurveyUserProducterInputDTO`):

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

### Example `property_data` (JSON for `PropertyInfoInputDTO`):

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

### Example `classification_user_data` (JSON for `ClassificationUserInputDTO`):

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

### Example `survey_data` (JSON for `CreateSurvey1InputDTO`):

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
  "user": "User Name",
  "worker_up": "Worker UP Name",
  "Household_size": "5",
  "other": "Some other info",
  "state": "PENDING"
}
```