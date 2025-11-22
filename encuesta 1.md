# Documentación de la Encuesta Tipo 1

Este documento contiene los `curl` para crear (POST) y actualizar (PUT) la Encuesta Tipo 1, junto con las estructuras JSON esperadas.

---

## 1. Crear Encuesta (POST)

Este endpoint permite crear una nueva encuesta tipo 1. La petición debe ser de tipo `multipart/form-data`.

**Endpoint:** `POST /api/v1/surveys/1`

### Comando `curl`

# Documentación de la Encuesta Tipo 1

Este documento contiene los `curl` para crear (POST) y actualizar (PUT) la Encuesta Tipo 1, junto con las estructuras JSON esperadas.

---

## 1. Crear Encuesta (POST)

Este endpoint permite crear una nueva encuesta tipo 1. La petición debe ser de tipo `multipart/form-data`.

**Endpoint:** `POST /api/v1/surveys/1`

### Comando `curl` (con archivos JSON)

```bash
curl --location 'http://127.0.0.1:8000/api/v1/surveys/1' 
--header 'accept: application/json' 
--form 'api_key="tu_api_key_aqui"' 
--form 'survey_data="@survey_data.json"' 
--form 'producter_data="@producter_data.json"' 
--form 'property_data="@property_data.json"' 
--form 'classification_user_data="@classification_user_data.json"' 
--form 'files="@/ruta/a/tu/imagen1.png"' 
--form 'files="@/ruta/a/tu/imagen2.jpg"'
```

### Comando `curl` completo (auto-contenido)

```bash
curl --location 'http://127.0.0.1:8000/api/v1/surveys/1' 
--header 'accept: application/json' 
--form 'api_key="tu_api_key_aqui"' 
--form 'survey_data={ 
    "medition_focalization": { 
        "control_resources": {"obervation": "Notas sobre control de recursos", "score": 4}, 
        "voice_influence_decision": {"obervation": "Notas sobre voz e influencia", "score": 3}, 
        "leadership_innovation": {"obervation": "Notas sobre liderazgo", "score": 5}, 
        "dialogue_knowledge": {"obervation": "Notas sobre diálogo de saberes", "score": 4} 
    }, 
    classification_user": {
        "development_human_capacity": {"observation": "Notes on human capacity", "score": 3},
        "development_social_capacity": {"observation": "Notes on social capacity", "score": 2},
        "access_adaptative_adoption_information": {"observation": "Notes on productive capacity", "score": 4},
        "sustainable_management_natural_resources": {"observation": "Notes on financial capacity", "score": 3},
        "participation_public_political": {"observation": "Notes on political capacity", "score": 2}
      },
    "objetive_accompaniment": "Objetivo del acompañamiento", 
    "initial_diagnosis": "Diagnóstico inicial del predio", 
    "recommendations_commitments": "Recomendaciones y compromisos adquiridos", 
    "observations_visited": "Observaciones generales de la visita", 
    "date_acompanamiento": "2025-11-21", 
    "hour_acompanamiento": "10:30:00", 
    "origen_register": "MOBILE", 
    "name_acompanamiento": "Nombre del técnico", 
    "visit_date": "2025-11-21T10:30:00", 
    "attended_by": "Nombre de quien atiende" 
}' 
--form 'producter_data={ 
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
    "representantive1_name": "Jane Doe Representante" 
}' 
--form 'property_data={ 
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
}' 
--form 'classification_user_data={ 
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
}' 
--form 'files="@/ruta/a/tu/imagen1.png"' 
--form 'files="@/ruta/a/tu/imagen2.jpg"'
```

### Estructuras JSON

A continuación se muestran los archivos JSON de ejemplo que se usarían en el comando `curl`.

**`survey_data.json`**
```json
{
    "medition_focalization": {
        "control_resources": {"obervation": "Notas sobre control de recursos", "score": 4},
        "voice_influence_decision": {"obervation": "Notas sobre voz e influencia", "score": 3},
        "leadership_innovation": {"obervation": "Notas sobre liderazgo", "score": 5},
        "dialogue_knowledge": {"obervation": "Notas sobre diálogo de saberes", "score": 4}
    },
    "objetive_accompaniment": "Objetivo del acompañamiento",
    "initial_diagnosis": "Diagnóstico inicial del predio",
    "recommendations_commitments": "Recomendaciones y compromisos adquiridos",
    "observations_visited": "Observaciones generales de la visita",
    "date_acompanamiento": "2025-11-21",
    "hour_acompanamiento": "10:30:00",
    "origen_register": "MOBILE",
    "name_acompanamiento": "Nombre del técnico",
    "visit_date": "2025-11-21T10:30:00",
    "attended_by": "Nombre de quien atiende"
}
```

**`producter_data.json`**
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
    "representantive1_name": "Jane Doe Representante"
}
```

**`property_data.json`**
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

**`classification_user_data.json`**
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

---

## 2. Actualizar Encuesta (PUT)

Este endpoint permite actualizar una encuesta tipo 1 existente. La petición debe ser de tipo `multipart/form-data`.

**Nota Importante:** El campo `classification_user_data` no se puede actualizar a través de este endpoint.

**Endpoint:** `PUT /api/v1/surveys/1/{survey_id}`

### Comando `curl` (con archivos JSON)

```bash
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/surveys/1/1' 
--header 'accept: application/json' 
--form 'api_key="tu_api_key_aqui"' 
--form 'survey_data="@survey_data_update.json"' 
--form 'producter_data="@producter_data_update.json"' 
--form 'property_data="@property_data_update.json"' 
--form 'files="@/ruta/a/tu/nueva_imagen1.png"'
```

### Comando `curl` completo (auto-contenido)

```bash
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/surveys/1/1' 
--header 'accept: application/json' 
--form 'api_key="tu_api_key_aqui"' 
--form 'survey_data={ 
    "medition_focalization": { 
        "control_resources": {"obervation": "Observación actualizada", "score": 5} 
    }, 
    "objetive_accompaniment": "Objetivo actualizado", 
    "initial_diagnosis": "Diagnóstico actualizado", 
    "recommendations_commitments": "Recomendaciones actualizadas", 
    "observations_visited": "Observaciones actualizadas", 
    "date_acompanamiento": "2025-11-22", 
    "hour_acompanamiento": "14:00:00", 
    "origen_register": "WEB", 
    "name_acompanamiento": "Otro Técnico", 
    "visit_date": "2025-11-22T14:00:00", 
    "attended_by": "Otra Persona" 
}' 
--form 'producter_data={ 
    "identification": "123456789", 
    "name": "John Doe Productor Actualizado", 
    "number_phone": "3109876543" 
}' 
--form 'property_data={ 
    "name": "Finca La Esperanza Renovada", 
    "village": "Bonda" 
}' 
--form 'files="@/ruta/a/tu/nueva_imagen1.png"'
```

### Estructuras JSON

A continuación se muestran los archivos JSON de ejemplo para la actualización.

**`survey_data_update.json`** (Contiene los campos de `UpdateSurvey1InputDTO`)
```json
{
    "medition_focalization": {
        "control_resources": {"obervation": "Observación actualizada", "score": 5}
    },
    "objetive_accompaniment": "Objetivo actualizado",
    "initial_diagnosis": "Diagnóstico actualizado",
    "recommendations_commitments": "Recomendaciones actualizadas",
    "observations_visited": "Observaciones actualizadas",
    "date_acompanamiento": "2025-11-22",
    "hour_acompanamiento": "14:00:00",
    "origen_register": "WEB",
    "name_acompanamiento": "Otro Técnico",
    "visit_date": "2025-11-22T14:00:00",
    "attended_by": "Otra Persona"
}
```

**`producter_data_update.json`** (Se pueden actualizar los datos del productor)
```json
{
    "identification": "123456789",
    "name": "John Doe Productor Actualizado",
    "number_phone": "3109876543"
}
```

**`property_data_update.json`** (Se pueden actualizar los datos del predio)
```json
{
    "name": "Finca La Esperanza Renovada",
    "village": "Bonda"
}
```


### Estructuras JSON

A continuación se muestran los archivos JSON de ejemplo que se usarían en el comando `curl`.

**`survey_data.json`**
```json
{
    "medition_focalization": {
        "control_resources": {"obervation": "Notas sobre control de recursos", "score": 4},
        "voice_influence_decision": {"obervation": "Notas sobre voz e influencia", "score": 3},
        "leadership_innovation": {"obervation": "Notas sobre liderazgo", "score": 5},
        "dialogue_knowledge": {"obervation": "Notas sobre diálogo de saberes", "score": 4}
    },
    "objetive_accompaniment": "Objetivo del acompañamiento",
    "initial_diagnosis": "Diagnóstico inicial del predio",
    "recommendations_commitments": "Recomendaciones y compromisos adquiridos",
    "observations_visited": "Observaciones generales de la visita",
    "date_acompanamiento": "2025-11-21",
    "hour_acompanamiento": "10:30:00",
    "origen_register": "MOBILE",
    "name_acompanamiento": "Nombre del técnico",
    "visit_date": "2025-11-21T10:30:00",
    "attended_by": "Nombre de quien atiende"
}
```

**`producter_data.json`**
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
    "representantive1_name": "Jane Doe Representante"
}
```

**`property_data.json`**
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

**`classification_user_data.json`**
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

---

## 2. Actualizar Encuesta (PUT)

Este endpoint permite actualizar una encuesta tipo 1 existente. La petición debe ser de tipo `multipart/form-data`.

**Nota Importante:** El campo `classification_user_data` no se puede actualizar a través de este endpoint.

**Endpoint:** `PUT /api/v1/surveys/1/{survey_id}`

### Comando `curl`

```bash
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/surveys/1/1' 
--header 'accept: application/json' 
--form 'api_key="tu_api_key_aqui"' 
--form 'survey_data="@survey_data_update.json"' 
--form 'producter_data="@producter_data_update.json"' 
--form 'property_data="@property_data_update.json"' 
--form 'files="@/ruta/a/tu/nueva_imagen1.png"'
```

### Estructuras JSON

A continuación se muestran los archivos JSON de ejemplo para la actualización.

**`survey_data_update.json`** (Contiene los campos de `UpdateSurvey1InputDTO`)
```json
{
    "medition_focalization": {
        "control_resources": {"obervation": "Observación actualizada", "score": 5}
    },
    "objetive_accompaniment": "Objetivo actualizado",
    "initial_diagnosis": "Diagnóstico actualizado",
    "recommendations_commitments": "Recomendaciones actualizadas",
    "observations_visited": "Observaciones actualizadas",
    "date_acompanamiento": "2025-11-22",
    "hour_acompanamiento": "14:00:00",
    "origen_register": "WEB",
    "name_acompanamiento": "Otro Técnico",
    "visit_date": "2025-11-22T14:00:00",
    "attended_by": "Otra Persona"
}
```

**`producter_data_update.json`** (Se pueden actualizar los datos del productor)
```json
{
    "identification": "123456789",
    "name": "John Doe Productor Actualizado",
    "number_phone": "3109876543"
}
```

**`property_data_update.json`** (Se pueden actualizar los datos del predio)
```json
{
    "name": "Finca La Esperanza Renovada",
    "village": "Bonda"
}
```