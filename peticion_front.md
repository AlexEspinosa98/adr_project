# Petición para Frontend – Encuestas 1, 2 y 3

Documento de referencia para que el equipo de frontend conozca exactamente qué se envía al backend en los endpoints `/api/v1/surveys`. Toda la información se validó contra los DTO y rutas reales del módulo `modules/surveys`.

## Reglas generales
- **Formato**: todas las peticiones son `multipart/form-data`.
- **Partes obligatorias en POST**:
  - `api_key`: cadena.
  - `survey_data`: JSON serializado (string).
  - `producter_data`: JSON serializado con datos del productor.
  - `property_data`: JSON serializado con datos del predio.
  - `classification_user_data`: solo aplica a los POST de survey 1 y 3.
  - `files`: lista de imágenes (mínimo 1). El backend asigna por orden: `photo_user`, `photo_interaction`, `photo_panorama`, `phono_extra_1`.
- **PUT**: mismos campos que el POST correspondiente, pero `files` es opcional y **no se acepta** `classification_user_data` en ningún PUT.
- **Endpoint base**: `http://45.65.200.114:8000/api/v1/surveys`.

---

## Survey 1 – Diagnóstico Inicial

### POST `/api/v1/surveys/1`
Partes:
1. `api_key`
2. `survey_data` → incluye `medition_focalization`, `classification_user` (estructura libre con `score` y `observation`), `objetive_accompaniment`, `initial_diagnosis`, `recommendations_commitments`, `observations_visited`, `date_hour_end`, `date_acompanamiento`, `hour_acompanamiento`, `origen_register`, `name_acompanamiento`, `visit_date`, `attended_by`.
3. `producter_data` → ver sección común más abajo.
4. `property_data` → ver sección común.
5. `classification_user_data` → puntajes numéricos (IDs) para cada dimensión (ver lista al final).
6. `files[]`

```bash
curl --location 'http://45.65.200.114:8000/api/v1/surveys/1' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data=@survey1_data.json' \
  --form 'producter_data=@producter.json' \
  --form 'property_data=@property.json' \
  --form 'classification_user_data=@classification.json' \
  --form 'files=@/path/photo_user.jpg' \
  --form 'files=@/path/photo_interaction.jpg' \
  --form 'files=@/path/photo_panorama.jpg' \
  --form 'files=@/path/photo_extra.jpg'
```

#### Curl completo (inline JSON)

```bash
curl --location 'http://45.65.200.114:8000/api/v1/surveys/1' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data="{
    \"medition_focalization\": {
      \"control_resources\": {\"obervation\": \"Notas sobre control\", \"score\": 4},
      \"voice_influence_decision\": {\"obervation\": \"Notas sobre voz\", \"score\": 3},
      \"leadership_innovation\": {\"obervation\": \"Notas sobre liderazgo\", \"score\": 5},
      \"dialogue_knowledge\": {\"obervation\": \"Notas sobre diálogo\", \"score\": 4}
    },
    \"classification_user\": {
      \"development_human_capacity\": {\"observation\": \"Observación\", \"score\": 3},
      \"development_social_capacity\": {\"observation\": \"Observación\", \"score\": 2},
      \"participation_public_political\": {\"observation\": \"Observación\", \"score\": 2},
      \"access_adaptative_adoption_information\": {\"observation\": \"Observación\", \"score\": 4},
      \"sustainable_management_natural_resources\": {\"observation\": \"Observación\", \"score\": 3}
    },
    \"objetive_accompaniment\": \"Objetivo del acompañamiento\",
    \"initial_diagnosis\": \"Diagnóstico inicial del predio\",
    \"recommendations_commitments\": \"Recomendaciones y compromisos\",
    \"observations_visited\": \"Observaciones generales de la visita\",
    \"date_acompanamiento\": \"2025-11-21\",
    \"hour_acompanamiento\": \"10:30:00\",
    \"origen_register\": \"MOBILE\",
    \"name_acompanamiento\": \"Nombre del técnico\",
    \"visit_date\": \"2025-11-21T10:30:00\",
    \"attended_by\": \"Nombre de quien atiende\"
  }"' \
  --form 'producter_data="{
    \"identification\": \"123456789\",
    \"name\": \"John Doe Productor\",
    \"type_id\": \"CC\",
    \"number_phone\": \"3001234567\",
    \"is_woman_rural\": false,
    \"is_young_rural\": true,
    \"ethnic_belonging\": \"Ninguna\",
    \"is_victim_conflict\": false,
    \"is_narp\": false,
    \"is_producer_organization_member\": true,
    \"organization_name\": \"ASOPROCAFE\",
    \"representantive1_name\": \"Jane Doe\"
  }"' \
  --form 'property_data="{
    \"name\": \"Finca La Esperanza\",
    \"latitude\": \"11.2345\",
    \"longitude\": \"-74.2012\",
    \"asnm\": \"120\",
    \"state\": \"Magdalena\",
    \"city\": \"Santa Marta\",
    \"village\": \"Minca\",
    \"linea_productive_primary\": \"Cafe\",
    \"linea_productive_secondary\": \"Aguacate\",
    \"area_in_production\": \"50\"
  }"' \
  --form 'classification_user_data="{
    \"main_productive_activity\": 1,
    \"secondary_productive_activities\": 2,
    \"tools_and_equipment\": 3,
    \"good_agricultural_practices\": 1,
    \"commercialization_structure\": 2,
    \"markets\": 3,
    \"added_value\": 1,
    \"records\": 2,
    \"labor_type\": 3,
    \"credit_and_banking\": 1,
    \"organization_membership\": 2,
    \"collective_activities\": 3,
    \"entrepreneurship_associativity\": 1,
    \"commercial_alliances\": 2,
    \"technical_support\": 3,
    \"quality_certifications\": 1,
    \"intellectual_property\": 2,
    \"access_information_sources\": 3,
    \"access_to_ict\": 1,
    \"use_of_ict_decision\": 2,
    \"ict_skills\": 3,
    \"knowledge_appropriation\": 1,
    \"environmental_practices\": 2,
    \"sustainable_practices\": 3,
    \"climate_change_adaptation\": 1,
    \"environmental_regulations\": 2,
    \"participation_mechanisms\": 3,
    \"participation_tools\": 1,
    \"political_social_control\": 2,
    \"community_self_management\": 3
  }"' \
  --form 'files=@"/path/photo_user.jpg"' \
  --form 'files=@"/path/photo_interaction.jpg"' \
  --form 'files=@"/path/photo_panorama.jpg"' \
  --form 'files=@"/path/photo_extra.jpg"'
```

`survey1_data.json` ejemplo:

```json
{
  "medition_focalization": {
    "control_resources": {"obervation": "Notas sobre control", "score": 4},
    "voice_influence_decision": {"obervation": "Notas sobre voz", "score": 3},
    "leadership_innovation": {"obervation": "Notas sobre liderazgo", "score": 5},
    "dialogue_knowledge": {"obervation": "Notas sobre diálogo", "score": 4}
  },
  "classification_user": {
    "development_human_capacity": {"observation": "Observación", "score": 3},
    "development_social_capacity": {"observation": "Observación", "score": 2},
    "participation_public_political": {"observation": "Observación", "score": 2},
    "access_adaptative_adoption_information": {"observation": "Observación", "score": 4},
    "sustainable_management_natural_resources": {"observation": "Observación", "score": 3}
  },
  "objetive_accompaniment": "Objetivo del acompañamiento",
  "initial_diagnosis": "Diagnóstico inicial del predio",
  "recommendations_commitments": "Recomendaciones y compromisos",
  "observations_visited": "Observaciones generales de la visita",
  "date_acompanamiento": "2025-11-21",
  "hour_acompanamiento": "10:30:00",
  "origen_register": "MOBILE",
  "name_acompanamiento": "Nombre del técnico",
  "visit_date": "2025-11-21T10:30:00",
  "attended_by": "Nombre de quien atiende"
}
```

`classification_user_data` (IDs numéricos):

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

### PUT `/api/v1/surveys/1/{survey_id}`
- Mismos campos que el POST **excepto** `classification_user_data` (no se envía).
- `files` solo si se reemplazan fotos (orden idéntico).

```bash
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/1/ID' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data=@survey1_update.json' \
  --form 'producter_data=@producter.json' \
  --form 'property_data=@property.json' \
  --form 'files=@/path/photo_user.jpg'
```

#### Curl completo (inline JSON)

```bash
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/1/ID' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data="{
    \"medition_focalization\": {
      \"control_resources\": {\"obervation\": \"Notas actualizadas\", \"score\": 4},
      \"voice_influence_decision\": {\"obervation\": \"Notas actualizadas\", \"score\": 3},
      \"leadership_innovation\": {\"obervation\": \"Notas actualizadas\", \"score\": 5},
      \"dialogue_knowledge\": {\"obervation\": \"Notas actualizadas\", \"score\": 4}
    },
    \"classification_user\": {
      \"development_human_capacity\": {\"observation\": \"Obs\", \"score\": 3},
      \"development_social_capacity\": {\"observation\": \"Obs\", \"score\": 2},
      \"participation_public_political\": {\"observation\": \"Obs\", \"score\": 2},
      \"access_adaptative_adoption_information\": {\"observation\": \"Obs\", \"score\": 4},
      \"sustainable_management_natural_resources\": {\"observation\": \"Obs\", \"score\": 3}
    },
    \"objetive_accompaniment\": \"Objetivo actualizado\",
    \"initial_diagnosis\": \"Diagnostico\",
    \"recommendations_commitments\": \"Recomendaciones\",
    \"observations_visited\": \"Observaciones\",
    \"date_acompanamiento\": \"2025-12-01\",
    \"hour_acompanamiento\": \"08:00:00\",
    \"origen_register\": \"MOBILE\",
    \"name_acompanamiento\": \"Nombre\",
    \"visit_date\": \"2025-12-01T08:00:00\",
    \"attended_by\": \"Persona\"
  }"' \
  --form 'producter_data="{
    \"identification\": \"123456789\",
    \"name\": \"John Doe Productor\",
    \"type_id\": \"CC\",
    \"number_phone\": \"3001234567\",
    \"is_woman_rural\": false,
    \"is_young_rural\": true,
    \"ethnic_belonging\": \"Ninguna\",
    \"is_victim_conflict\": false,
    \"is_narp\": false,
    \"is_producer_organization_member\": true,
    \"organization_name\": \"ASOPROCAFE\",
    \"representantive1_name\": \"Jane Doe\"
  }"' \
  --form 'property_data="{
    \"name\": \"Finca La Esperanza\",
    \"latitude\": \"11.2345\",
    \"longitude\": \"-74.2012\",
    \"asnm\": \"120\",
    \"state\": \"Magdalena\",
    \"city\": \"Santa Marta\",
    \"village\": \"Minca\",
    \"linea_productive_primary\": \"Cafe\",
    \"linea_productive_secondary\": \"Aguacate\",
    \"area_in_production\": \"50\"
  }"' \
  --form 'files=@"/path/photo_user.jpg"'
```

---

## Survey 2 – Seguimiento

### POST `/api/v1/surveys/2`
Partes:
1. `api_key`
2. `survey_data` → campos aceptados por `CreateSurvey2InputDTO`: `objective_accompaniment`, `visit_development_follow_up_activities`, `previous_visit_recommendations_fulfilled`, `recommendations_commitments`, `observations_visited`, `objective`, `visit_followup`, `fulfilled_previous_recommendations`, `new_recommendations`, `observations_seg`, `register_coinnovation`, `local_practice_tool_technology_coinnovation_identified`, `local_coinovation_or_technology_record`, `name_innovation`, `description_innovation`, `problem_solution_innovation`, `origin_and_developers`, `materials_and_resources`, `process_functioning`, `potential_replication`, `observations_extensionist`, `date_hour_end`, `socilization_next_event`, `visit_date`, `attended_by`, `date_acompanamiento`, `hour_acompanamiento`, `origen_register`, `name_acompanamiento`.
3. `producter_data`
4. `property_data`
5. `files[]`

```bash
curl --location 'http://45.65.200.114:8000/api/v1/surveys/2' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data=@survey2_data.json' \
  --form 'producter_data=@producter.json' \
  --form 'property_data=@property.json' \
  --form 'files=@/path/photo_user.jpg' \
  --form 'files=@/path/photo_interaction.jpg'
```

#### Curl completo (inline JSON)

```bash
curl --location 'http://45.65.200.114:8000/api/v1/surveys/2' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data="{
    \"objective_accompaniment\": \"Objetivo del seguimiento\",
    \"visit_development_follow_up_activities\": \"Actividades realizadas\",
    \"previous_visit_recommendations_fulfilled\": true,
    \"recommendations_commitments\": \"Nuevas recomendaciones\",
    \"observations_visited\": \"Observaciones de la visita\",
    \"objective\": \"Objetivo visita anterior\",
    \"visit_followup\": \"Avances, dificultades, tareas pendientes\",
    \"fulfilled_previous_recommendations\": true,
    \"new_recommendations\": \"Basadas en el seguimiento\",
    \"observations_seg\": \"Observaciones del seguimiento\",
    \"register_coinnovation\": \"Descripción de co-innovación\",
    \"local_practice_tool_technology_coinnovation_identified\": true,
    \"local_coinovation_or_technology_record\": true,
    \"name_innovation\": \"Sistema de riego por goteo\",
    \"description_innovation\": \"Descripción de la innovación\",
    \"problem_solution_innovation\": \"Problema que soluciona\",
    \"origin_and_developers\": \"Productores locales\",
    \"materials_and_resources\": \"Materiales usados\",
    \"process_functioning\": \"Cómo funciona\",
    \"potential_replication\": \"Potencial de réplica\",
    \"observations_extensionist\": \"Notas del extensionista\",
    \"date_hour_end\": \"2025-11-08T12:00:00\",
    \"socilization_next_event\": \"Próximo evento\",
    \"date_acompanamiento\": \"2025-11-08\",
    \"hour_acompanamiento\": \"11:00\",
    \"origen_register\": \"MOBILE\",
    \"name_acompanamiento\": \"Seguimiento 1\",
    \"visit_date\": \"2025-11-08T11:00:00\",
    \"attended_by\": \"Jane Doe\"
  }"' \
  --form 'producter_data="{
    \"identification\": \"123456789\",
    \"name\": \"John Doe Productor\",
    \"type_id\": \"CC\",
    \"number_phone\": \"3001234567\",
    \"is_woman_rural\": false,
    \"is_young_rural\": true,
    \"ethnic_belonging\": \"Ninguna\",
    \"is_victim_conflict\": false,
    \"is_narp\": false,
    \"is_producer_organization_member\": true,
    \"organization_name\": \"ASOPROCAFE\",
    \"representantive1_name\": \"Jane Doe\"
  }"' \
  --form 'property_data="{
    \"name\": \"Finca La Esperanza\",
    \"latitude\": \"11.2345\",
    \"longitude\": \"-74.2012\",
    \"asnm\": \"120\",
    \"state\": \"Magdalena\",
    \"city\": \"Santa Marta\",
    \"village\": \"Minca\",
    \"linea_productive_primary\": \"Cafe\",
    \"linea_productive_secondary\": \"Aguacate\",
    \"area_in_production\": \"50\"
  }"' \
  --form 'files=@"/path/photo_user.jpg"' \
  --form 'files=@"/path/photo_interaction.jpg"'
```

`survey2_data.json` ejemplo:

```json
{
  "objective_accompaniment": "Objetivo del seguimiento",
  "visit_development_follow_up_activities": "Actividades realizadas",
  "previous_visit_recommendations_fulfilled": true,
  "recommendations_commitments": "Nuevas recomendaciones",
  "observations_visited": "Observaciones de la visita",
  "objective": "Objetivo visita anterior",
  "visit_followup": "Avances, dificultades, tareas pendientes",
  "fulfilled_previous_recommendations": true,
  "new_recommendations": "Basadas en el seguimiento",
  "observations_seg": "Observaciones del seguimiento",
  "register_coinnovation": "Descripción de co-innovación",
  "local_practice_tool_technology_coinnovation_identified": true,
  "local_coinovation_or_technology_record": true,
  "name_innovation": "Sistema de riego por goteo",
  "description_innovation": "Descripción de la innovación",
  "problem_solution_innovation": "Problema que soluciona",
  "origin_and_developers": "Productores locales",
  "materials_and_resources": "Materiales usados",
  "process_functioning": "Cómo funciona",
  "potential_replication": "Potencial de réplica",
  "observations_extensionist": "Notas del extensionista",
  "date_hour_end": "2025-11-08T12:00:00",
  "socilization_next_event": "Próximo evento",
  "date_acompanamiento": "2025-11-08",
  "hour_acompanamiento": "11:00",
  "origen_register": "MOBILE",
  "name_acompanamiento": "Seguimiento 1",
  "visit_date": "2025-11-08T11:00:00",
  "attended_by": "Jane Doe"
}
```

### PUT `/api/v1/surveys/2/{survey_id}`
- Estructura exactamente igual al POST (mismos campos en `survey_data`, `producter_data`, `property_data`).
- `files` opcional para reemplazar fotos.

```bash
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/2/ID' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data=@survey2_update.json' \
  --form 'producter_data=@producter.json' \
  --form 'property_data=@property.json'
```

#### Curl completo (inline JSON)

```bash
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/2/ID' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data="{
    \"objective_accompaniment\": \"Objetivo actualizado\",
    \"visit_development_follow_up_activities\": \"Actividades\",
    \"previous_visit_recommendations_fulfilled\": false,
    \"recommendations_commitments\": \"Compromisos\",
    \"observations_visited\": \"Observaciones\",
    \"objective\": \"Objetivo\",
    \"visit_followup\": \"Seguimiento\",
    \"fulfilled_previous_recommendations\": true,
    \"new_recommendations\": \"Nuevas\",
    \"observations_seg\": \"Notas\",
    \"register_coinnovation\": \"Registro\",
    \"local_practice_tool_technology_coinnovation_identified\": false,
    \"local_coinovation_or_technology_record\": true,
    \"name_innovation\": \"Nombre\",
    \"description_innovation\": \"Descripción\",
    \"problem_solution_innovation\": \"Problema\",
    \"origin_and_developers\": \"Origen\",
    \"materials_and_resources\": \"Materiales\",
    \"process_functioning\": \"Proceso\",
    \"potential_replication\": \"Potencial\",
    \"observations_extensionist\": \"Observaciones\",
    \"date_hour_end\": \"2025-12-10T10:00:00\",
    \"socilization_next_event\": \"Evento\",
    \"date_acompanamiento\": \"2025-12-10\",
    \"hour_acompanamiento\": \"10:00\",
    \"origen_register\": \"WEB\",
    \"name_acompanamiento\": \"Seguimiento 2\",
    \"visit_date\": \"2025-12-10T10:00:00\",
    \"attended_by\": \"Carlos Gomez\"
  }"' \
  --form 'producter_data="{
    \"identification\": \"123456789\",
    \"name\": \"John Doe Productor\",
    \"type_id\": \"CC\",
    \"number_phone\": \"3001234567\",
    \"is_woman_rural\": false,
    \"is_young_rural\": true,
    \"ethnic_belonging\": \"Ninguna\",
    \"is_victim_conflict\": false,
    \"is_narp\": false,
    \"is_producer_organization_member\": true,
    \"organization_name\": \"ASOPROCAFE\",
    \"representantive1_name\": \"Jane Doe\"
  }"' \
  --form 'property_data="{
    \"name\": \"Finca La Esperanza\",
    \"latitude\": \"11.2345\",
    \"longitude\": \"-74.2012\",
    \"asnm\": \"120\",
    \"state\": \"Magdalena\",
    \"city\": \"Santa Marta\",
    \"village\": \"Minca\",
    \"linea_productive_primary\": \"Cafe\",
    \"linea_productive_secondary\": \"Aguacate\",
    \"area_in_production\": \"50\"
  }"' \
  --form 'files=@"/path/photo_user.jpg"'
```

---

## Survey 3 – Cierre

### POST `/api/v1/surveys/3`
Partes:
1. `api_key`
2. `survey_data` → `medition_focalization`, `classification_user`, `objetive_accompaniment`, `development_accompaniment`, `final_diagnosis`, `recommendations_commitments`, `observations_visited`, `date_hour_end`, `socialization_events_group`, `not_agend_new_visit`, `date_acompanamiento`, `hour_acompanamiento`, `origen_register`, `name_acompanamiento`, `visit_date`, `attended_by`.
3. `producter_data`
4. `property_data`
5. `classification_user_data` → mismos IDs numéricos que survey 1.
6. `files[]`

```bash
curl --location 'http://45.65.200.114:8000/api/v1/surveys/3' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data=@survey3_data.json' \
  --form 'producter_data=@producter.json' \
  --form 'property_data=@property.json' \
  --form 'classification_user_data=@classification.json' \
  --form 'files=@/path/photo_user.jpg'
```

#### Curl completo (inline JSON)

```bash
curl --location 'http://45.65.200.114:8000/api/v1/surveys/3' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data="{
    \"classification_user\": {
      \"development_human_capacity\": {\"observation\": \"Final\", \"score\": 4},
      \"development_social_capacity\": {\"observation\": \"Final\", \"score\": 3},
      \"access_adaptative_adoption_information\": {\"observation\": \"Final\", \"score\": 5},
      \"sustainable_management_natural_resources\": {\"observation\": \"Final\", \"score\": 4},
      \"participation_public_political\": {\"observation\": \"Final\", \"score\": 3}
    },
    \"medition_focalization\": {
      \"control_resources\": {\"obervation\": \"Cierre\", \"score\": 5},
      \"voice_influence_decision\": {\"obervation\": \"Cierre\", \"score\": 4},
      \"leadership_innovation\": {\"obervation\": \"Cierre\", \"score\": 5},
      \"dialogue_knowledge\": {\"obervation\": \"Cierre\", \"score\": 4}
    },
    \"objetive_accompaniment\": \"Objetivo de cierre\",
    \"development_accompaniment\": \"Desarrollo del acompañamiento final\",
    \"final_diagnosis\": \"Diagnóstico final\",
    \"recommendations_commitments\": \"Recomendaciones finales\",
    \"observations_visited\": \"Observaciones finales\",
    \"date_hour_end\": \"2025-11-09T13:00:00\",
    \"socialization_events_group\": \"Socialización con el grupo\",
    \"not_agend_new_visit\": \"No se agenda nueva visita\",
    \"date_acompanamiento\": \"2025-11-09\",
    \"hour_acompanamiento\": \"12:00\",
    \"origen_register\": \"WEB\",
    \"name_acompanamiento\": \"Diagnostico Final\",
    \"visit_date\": \"2025-11-09T12:00:00\",
    \"attended_by\": \"John Smith\"
  }"' \
  --form 'producter_data="{
    \"identification\": \"123456789\",
    \"name\": \"John Doe Productor\",
    \"type_id\": \"CC\",
    \"number_phone\": \"3001234567\",
    \"is_woman_rural\": false,
    \"is_young_rural\": true,
    \"ethnic_belonging\": \"Ninguna\",
    \"is_victim_conflict\": false,
    \"is_narp\": false,
    \"is_producer_organization_member\": true,
    \"organization_name\": \"ASOPROCAFE\",
    \"representantive1_name\": \"Jane Doe\"
  }"' \
  --form 'property_data="{
    \"name\": \"Finca La Esperanza\",
    \"latitude\": \"11.2345\",
    \"longitude\": \"-74.2012\",
    \"asnm\": \"120\",
    \"state\": \"Magdalena\",
    \"city\": \"Santa Marta\",
    \"village\": \"Minca\",
    \"linea_productive_primary\": \"Cafe\",
    \"linea_productive_secondary\": \"Aguacate\",
    \"area_in_production\": \"50\"
  }"' \
  --form 'classification_user_data="{
    \"main_productive_activity\": 1,
    \"secondary_productive_activities\": 2,
    \"tools_and_equipment\": 3,
    \"good_agricultural_practices\": 1,
    \"commercialization_structure\": 2,
    \"markets\": 3,
    \"added_value\": 1,
    \"records\": 2,
    \"labor_type\": 3,
    \"credit_and_banking\": 1,
    \"organization_membership\": 2,
    \"collective_activities\": 3,
    \"entrepreneurship_associativity\": 1,
    \"commercial_alliances\": 2,
    \"technical_support\": 3,
    \"quality_certifications\": 1,
    \"intellectual_property\": 2,
    \"access_information_sources\": 3,
    \"access_to_ict\": 1,
    \"use_of_ict_decision\": 2,
    \"ict_skills\": 3,
    \"knowledge_appropriation\": 1,
    \"environmental_practices\": 2,
    \"sustainable_practices\": 3,
    \"climate_change_adaptation\": 1,
    \"environmental_regulations\": 2,
    \"participation_mechanisms\": 3,
    \"participation_tools\": 1,
    \"political_social_control\": 2,
    \"community_self_management\": 3
  }"' \
  --form 'files=@"/path/photo_user.jpg"' \
  --form 'files=@"/path/photo_interaction.jpg"' \
  --form 'files=@"/path/photo_panorama.jpg"' \
  --form 'files=@"/path/photo_extra.jpg"'
```

`survey3_data.json` ejemplo:

```json
{
  "classification_user": {
    "development_human_capacity": {"observation": "Observación final", "score": 4},
    "development_social_capacity": {"observation": "Observación final", "score": 3},
    "access_adaptative_adoption_information": {"observation": "Observación final", "score": 5},
    "sustainable_management_natural_resources": {"observation": "Observación final", "score": 4},
    "participation_public_political": {"observation": "Observación final", "score": 3}
  },
  "medition_focalization": {
    "control_resources": {"obervation": "Cierre", "score": 5},
    "voice_influence_decision": {"obervation": "Cierre", "score": 4},
    "leadership_innovation": {"obervation": "Cierre", "score": 5},
    "dialogue_knowledge": {"obervation": "Cierre", "score": 4}
  },
  "objetive_accompaniment": "Objetivo de cierre",
  "development_accompaniment": "Desarrollo del acompañamiento final",
  "final_diagnosis": "Diagnóstico final",
  "recommendations_commitments": "Recomendaciones finales",
  "observations_visited": "Observaciones finales",
  "date_hour_end": "2025-11-09T13:00:00",
  "socialization_events_group": "Socialización con el grupo",
  "not_agend_new_visit": "No se agenda nueva visita",
  "date_acompanamiento": "2025-11-09",
  "hour_acompanamiento": "12:00",
  "origen_register": "WEB",
  "name_acompanamiento": "Diagnóstico final",
  "visit_date": "2025-11-09T12:00:00",
  "attended_by": "John Smith"
}
```

### PUT `/api/v1/surveys/3/{survey_id}`
- Igual al POST pero sin `classification_user_data`.
- `files` opcional para actualizar fotos.

```bash
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/3/ID' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data=@survey3_update.json' \
  --form 'producter_data=@producter.json' \
  --form 'property_data=@property.json'
```

#### Curl completo (inline JSON)

```bash
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/3/ID' \
  --header 'accept: application/json' \
  --form 'api_key="API_KEY_AQUI"' \
  --form 'survey_data="{
    \"classification_user\": {
      \"development_human_capacity\": {\"observation\": \"Final\", \"score\": 4},
      \"development_social_capacity\": {\"observation\": \"Final\", \"score\": 3},
      \"access_adaptative_adoption_information\": {\"observation\": \"Final\", \"score\": 5},
      \"sustainable_management_natural_resources\": {\"observation\": \"Final\", \"score\": 4},
      \"participation_public_political\": {\"observation\": \"Final\", \"score\": 3}
    },
    \"medition_focalization\": {
      \"control_resources\": {\"obervation\": \"Cierre\", \"score\": 5},
      \"voice_influence_decision\": {\"obervation\": \"Cierre\", \"score\": 4},
      \"leadership_innovation\": {\"obervation\": \"Cierre\", \"score\": 5},
      \"dialogue_knowledge\": {\"obervation\": \"Cierre\", \"score\": 4}
    },
    \"objetive_accompaniment\": \"Objetivo\",
    \"development_accompaniment\": \"Desarrollo\",
    \"final_diagnosis\": \"Diagnostico final\",
    \"recommendations_commitments\": \"Recomendaciones\",
    \"observations_visited\": \"Observaciones\",
    \"date_hour_end\": \"2025-12-12T13:00:00\",
    \"socialization_events_group\": \"Socializacion\",
    \"not_agend_new_visit\": \"Sin nueva visita\",
    \"date_acompanamiento\": \"2025-12-12\",
    \"hour_acompanamiento\": \"12:00\",
    \"origen_register\": \"WEB\",
    \"name_acompanamiento\": \"Cierre final\",
    \"visit_date\": \"2025-12-12T12:00:00\",
    \"attended_by\": \"John Smith\"
  }"' \
  --form 'producter_data="{
    \"identification\": \"123456789\",
    \"name\": \"John Doe Productor\",
    \"type_id\": \"CC\",
    \"number_phone\": \"3001234567\",
    \"is_woman_rural\": false,
    \"is_young_rural\": true,
    \"ethnic_belonging\": \"Ninguna\",
    \"is_victim_conflict\": false,
    \"is_narp\": false,
    \"is_producer_organization_member\": true,
    \"organization_name\": \"ASOPROCAFE\",
    \"representantive1_name\": \"Jane Doe\"
  }"' \
  --form 'property_data="{
    \"name\": \"Finca La Esperanza\",
    \"latitude\": \"11.2345\",
    \"longitude\": \"-74.2012\",
    \"asnm\": \"120\",
    \"state\": \"Magdalena\",
    \"city\": \"Santa Marta\",
    \"village\": \"Minca\",
    \"linea_productive_primary\": \"Cafe\",
    \"linea_productive_secondary\": \"Aguacate\",
    \"area_in_production\": \"50\"
  }"' \
  --form 'files=@"/path/photo_user.jpg"'
```

---

## Datos comunes

### `producter_data`

```json
{
  "identification": "123456789",
  "name": "John Doe Productor",
  "type_id": "CC",
  "number_phone": "3001234567",
  "is_woman_rural": false,
  "is_young_rural": true,
  "ethnic_belonging": "Ninguna",
  "is_victim_conflict": false,
  "is_narp": false,
  "is_producer_organization_member": true,
  "organization_name": "ASOPROCAFÉ",
  "representantive1_name": "Jane Doe"
}
```

### `property_data`

```json
{
  "name": "Finca La Esperanza",
  "latitude": "11.2345",
  "longitude": "-74.2012",
  "asnm": "120",
  "state": "Magdalena",
  "city": "Santa Marta",
  "village": "Minca",
  "linea_productive_primary": "Café",
  "linea_productive_secondary": "Aguacate",
  "area_in_production": "50"
}
```

### `classification_user_data`
Se usa únicamente en los POST de surveys 1 y 3. Campos permitidos (todos numéricos): `main_productive_activity`, `secondary_productive_activities`, `tools_and_equipment`, `good_agricultural_practices`, `commercialization_structure`, `markets`, `added_value`, `records`, `labor_type`, `credit_and_banking`, `organization_membership`, `collective_activities`, `entrepreneurship_associativity`, `commercial_alliances`, `technical_support`, `quality_certifications`, `intellectual_property`, `access_information_sources`, `access_to_ict`, `use_of_ict_decision`, `ict_skills`, `knowledge_appropriation`, `environmental_practices`, `sustainable_practices`, `climate_change_adaptation`, `environmental_regulations`, `participation_mechanisms`, `participation_tools`, `political_social_control`, `community_self_management`.

---

### Resumen rápido
- **POST**: siempre `api_key`, `survey_data`, `producter_data`, `property_data`, `files` (y `classification_user_data` para survey 1/3).
- **PUT**: mismo payload que el POST equivalente sin `classification_user_data`; `files` solo si cambian imágenes.
- Base URL y rutas diferenciadas por tipo: `/1`, `/2`, `/3` y `/type/{survey_id}` para actualizaciones.
