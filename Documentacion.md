Documentación de la Encuesta Tipo 1
Este documento contiene los comandos curl para crear (POST) y actualizar (PUT) la Encuesta Tipo 1, junto con las estructuras JSON esperadas.
1. Crear Encuesta (POST)
Este endpoint permite crear una nueva encuesta tipo 1. La petición debe ser de tipo multipart/form-data.
Endpoint: POST /api/v1/surveys/1
1.1 Comando curl (usando archivos JSON)
curl --location 'http://127.0.0.1:8000/api/v1/surveys/1' \
  --header 'accept: application/json' \
  --form 'api_key="tu_api_key_aqui"' \
  --form 'survey_data=@survey_data.json' \
  --form 'producter_data=@producter_data.json' \
  --form 'property_data=@property_data.json' \
  --form 'classification_user_data=@classification_user_data.json' \
  --form 'files=@/ruta/a/tu/imagen1.png' \
  --form 'files=@/ruta/a/tu/imagen2.jpg'
1.2 Comando curl completo (auto-contenido)
curl --location 'http://127.0.0.1:8000/api/v1/surveys/1' \
  --header 'accept: application/json' \
  --form 'api_key="tu_api_key_aqui"' \
  --form 'survey_data={
    "medition_focalization": {
      "control_resources": { "obervation": "Notas sobre control de recursos", "score": 4 },
      "voice_influence_decision": { "obervation": "Notas sobre voz e influencia", "scorea": 3 },
      "leadership_innovation": { "obervation": "Notas sobre liderazgo", "score": 5 },
      "dialogue_knowledge": { "obervation": "Notas sobre diálogo de saberes", "score": 4 }
    },
    "classification_user": {
      "main_productive_activity": { "observation": "Notes on main productive activity", "score": 1 },
      "secondary_productive_activities": { "observation": "Notes on secondary productive activities", "score": 2 },
      "tools_and_equipment": { "observation": "Notes on tools and equipment", "score": 3 },
      "good_agricultural_practices": { "observation": "Notes on good agricultural practices", "score": 1 },
      "commercialization_structure": { "observation": "Notes on commercialization structure", "score": 2 },
      "markets": { "observation": "Notes on markets", "score": 3 },
      "added_value": { "observation": "Notes on added value", "score": 1 },
      "records": { "observation": "Notes on records", "score": 2 },
      "labor_type": { "observation": "Notes on labor type", "score": 3 },
      "credit_and_banking": { "observation": "Notes on credit and banking", "score": 1 },
      "organization_membership": { "observation": "Notes on organization membership", "score": 2 },
      "collective_activities": { "observation": "Notes on collective activities", "score": 3 },
      "entrepreneurship_associativity": { "observation": "Notes on entrepreneurship and associativity", "score": 1 },
      "commercial_alliances": { "observation": "Notes on commercial alliances", "score": 2 },
      "technical_support": { "observation": "Notes on technical support", "score": 3 },
      "quality_certifications": { "observation": "Notes on quality certifications", "score": 1 },
      "intellectual_property": { "observation": "Notes on intellectual property", "score": 2 },
      "access_information_sources": { "observation": "Notes on access to information sources", "score": 3 },
      "access_to_ict": { "observation": "Notes on access to ICT", "score": 1 },
      "use_of_ict_decision": { "observation": "Notes on use of ICT in decision making", "score": 2 },
      "ict_skills": { "observation": "Notes on ICT skills", "score": 3 },
      "knowledge_appropriation": { "observation": "Notes on knowledge appropriation", "score": 1 },
      "environmental_practices": { "observation": "Notes on environmental practices", "score": 2 },
      "sustainable_practices": { "observation": "Notes on sustainable practices", "score": 3 },
      "climate_change_adaptation": { "observation": "Notes on climate change adaptation", "score": 1 },
      "environmental_regulations": { "observation": "Notes on environmental regulations", "score": 2 },
      "participation_mechanisms": { "observation": "Notes on participation mechanisms", "score": 3 },
      "participation_tools": { "observation": "Notes on participation tools", "score": 1 },
      "political_social_control": { "observation": "Notes on political and social control", "score": 2 },
      "community_self_management": { "observation": "Notes on community self management", "score": 3 }
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
  }' \
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
  }' \
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
  }' \
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
  }' \
  --form 'files=@/ruta/a/tu/imagen1.png' \
  --form 'files=@/ruta/a/tu/imagen2.jpg'
2. Actualizar Encuesta (PUT)
Este endpoint permite actualizar una encuesta tipo 1 existente. La petición debe ser de tipo multipart/form-data.
Nota importante: el campo classification_user_data no se envía en el PUT como parte del multipart/form-data.
Endpoint: PUT /api/v1/surveys/1/{survey_id}
2.1 Comando curl (usando archivos JSON)
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/surveys/1/1' \
  --header 'accept: application/json' \
  --form 'api_key="tu_api_key_aqui"' \
  --form 'survey_data=@survey_data_update.json' \
  --form 'producter_data=@producter_data_update.json' \
  --form 'property_data=@property_data_update.json' \
  --form 'files=@/ruta/a/tu/nueva_imagen1.png'
2.2 Comando curl completo (auto-contenido)
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/surveys/1/1' \
  --header 'accept: application/json' \
  --form 'api_key="tu_api_key_aqui"' \
  --form 'survey_data={
    "medition_focalization": {
      "control_resources": { "obervation": "Notas sobre control de recursos", "score": 4 },
      "voice_influence_decision": { "obervation": "Notas sobre voz e influencia", "score": 3 },
      "leadership_innovation": { "obervation": "Notas sobre liderazgo", "score": 5 },
      "dialogue_knowledge": { "obervation": "Notas sobre diálogo de saberes", "score": 4 }
    },
    "classification_user": {
      "main_productive_activity": { "observation": "Notes on main productive activity", "score": 1 },
      "secondary_productive_activities": { "observation": "Notes on secondary productive activities", "score": 2 },
      "tools_and_equipment": { "observation": "Notes on tools and equipment", "score": 3 },
      "good_agricultural_practices": { "observation": "Notes on good agricultural practices", "score": 1 },
      "commercialization_structure": { "observation": "Notes on commercialization structure", "score": 2 },
      "markets": { "observation": "Notes on markets", "score": 3 },
      "added_value": { "observation": "Notes on added value", "score": 1 },
      "records": { "observation": "Notes on records", "score": 2 },
      "labor_type": { "observation": "Notes on labor type", "score": 3 },
      "credit_and_banking": { "observation": "Notes on credit and banking", "score": 1 },
      "organization_membership": { "observation": "Notes on organization membership", "score": 2 },
      "collective_activities": { "observation": "Notes on collective activities", "score": 3 },
      "entrepreneurship_associativity": { "observation": "Notes on entrepreneurship and associativity", "score": 1 },
      "commercial_alliances": { "observation": "Notes on commercial alliances", "score": 2 },
      "technical_support": { "observation": "Notes on technical support", "score": 3 },
      "quality_certifications": { "observation": "Notes on quality certifications", "score": 1 },
      "intellectual_property": { "observation": "Notes on intellectual property", "score": 2 },
      "access_information_sources": { "observation": "Notes on access to information sources", "score": 3 },
      "access_to_ict": { "observation": "Notes on access to ICT", "score": 1 },
      "use_of_ict_decision": { "observation": "Notes on use of ICT in decision making", "score": 2 },
      "ict_skills": { "observation": "Notes on ICT skills", "score": 3 },
      "knowledge_appropriation": { "observation": "Notes on knowledge appropriation", "score": 1 },
      "environmental_practices": { "observation": "Notes on environmental practices", "score": 2 },
      "sustainable_practices": { "observation": "Notes on sustainable practices", "score": 3 },
      "climate_change_adaptation": { "observation": "Notes on climate change adaptation", "score": 1 },
      "environmental_regulations": { "observation": "Notes on environmental regulations", "score": 2 },
      "participation_mechanisms": { "observation": "Notes on participation mechanisms", "score": 3 },
      "participation_tools": { "observation": "Notes on participation tools", "score": 1 },
      "political_social_control": { "observation": "Notes on political and social control", "score": 2 },
      "community_self_management": { "observation": "Notes on community self management", "score": 3 }
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
  }' \
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
  }' \
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


✅ 1. MAPPER COMPLETO PARA EL FRONT
Este mapper representa TODO lo que necesitas enviar al backend en /api/v1/surveys/2.
📌 1.1. survey_data (Visita 2)
Descripción del campo → Nombre en español → Nombre en inglés (clave usada en API)
{
  "objective_accompaniment": "Objetivo del acompañamiento (V2)",
  "visit_development_follow_up_activities": "Desarrollo de la visita y actividades de seguimiento",
  "previous_visit_recommendations_fulfilled": "¿Se cumplieron las recomendaciones de la visita anterior?",
  "recommendations_commitments": "Recomendaciones y compromisos",
  "observations_visited": "Observaciones de la visita",
  "objective": "Objetivo de la visita anterior",
  "visit_followup": "Avances, dificultades y tareas pendientes",
  "fulfilled_previous_recommendations": "Confirmación si cumplió recomendaciones previas",
  "new_recommendations": "Nuevas recomendaciones basadas en el seguimiento",
  "observations_seg": "Observaciones del seguimiento",
  "register_coinnovation": "Registro de co-innovación",
  "local_practice_tool_technology_coinnovation_identified": "¿Identifica co-innovación?",
  "local_coinovation_or_technology_record": "¿Autoriza registro de innovación?",
  "name_innovation": "Nombre de la innovación",
  "description_innovation": "Descripción de la innovación",
  "problem_solution_innovation": "Problema o necesidad que soluciona",
  "origin_and_developers": "Origen y desarrolladores",
  "materials_and_resources": "Materiales e insumos",
  "process_functioning": "Proceso o funcionamiento",
  "potential_replication": "Potencial de réplica",
  "observations_extensionist": "Observaciones del extensionista",
  "date_hour_end": "Fecha y hora final de la visita 2",
  "socilization_next_event": "Socialización del próximo evento",
  "copy_documentation_delivered": "¿Se entregó copia del formato?",
  "date_acompanamiento": "Fecha del acompañamiento",
  "hour_acompanamiento": "Hora del acompañamiento",
  "origen_register": "Origen del registro (APP/WEB)",
  "name_acompanamiento": "Nombre del acompañamiento",
  "type_acompanamiento": "Tipo de acompañamiento",
  "other_acompanamiento": "Otro tipo de acompañamiento",
  "visit_date": "Fecha y hora de la visita",
  "attended_by": "Persona que atendió",
  "user": "Usuario asociado",
  "worker_up": "Trabajador UP",
  "Household_size": "Tamaño del hogar",
  "other": "Otro"
}
 
📌 1.2. producter_data (Datos del productor)
{
  "identification": "Número de identificación",
  "name": "Nombre completo",
  "type_id": "Tipo de documento",
  "number_phone": "Número telefónico",
  "is_woman_rural": "¿Es mujer rural?",
  "is_young_rural": "¿Es joven rural?",
  "ethnic_belonging": "Pertenencia étnica",
  "is_victim_conflict": "¿Es víctima del conflicto?",
  "is_narp": "¿Pertenece a comunidad NARP?",
  "is_producer_organization_member": "¿Es miembro de organización?",
  "organization_name": "Nombre de la organización",
  "representantive1_name": "Nombre del representante"
}
 
📌 1.3. property_data (Predio)
{
  "name": "Nombre del predio",
  "latitude": "Latitud",
  "longitude": "Longitud",
  "asnm": "Altura sobre el nivel del mar",
  "state": "Departamento",
  "city": "Municipio",
  "village": "Corregimiento/Vereda",
  "linea_productive_primary": "Línea productiva principal",
  "linea_productive_secondary": "Línea productiva secundaria",
  "area_in_production": "Área en producción"
}
 
📌 1.4. files
Lista de imágenes subidas:
•	Foto del usuario
•	Foto de interacción
•	Foto panorámica
•	Foto del acompañamiento
•	Fotos de co-innovación
El backend soporta varios files en multipart/form-data.
 
✅ 2. JSON FINAL PARA HACER EL REQUEST
Aquí tienes exactamente lo que debes enviar al backend:
{
  "api_key": "string",
  "survey_data": { ...mapper_survey_data... },
  "producter_data": { ...mapper_producter_data... },
  "property_data": { ...mapper_property_data... },
  "files": [ "file1", "file2", "file3", "file4" ]
}
 
✅ 3. RESPONSE EXACTO DEL BACKEND
Este es el response que recibirás:
{
  "data": {
    "id": 1
  },
  "message": "Survey 2 created successfully",
  "success": true
}
 
✅ 4. MAPPER FINAL PARA EL FRONT (LISTO PARA FORMULARIO REACT/VUE/ANGULAR)
Estructura recomendada
{
  "survey2": {
    "objective_accompaniment": "",
    "visit_development_follow_up_activities": "",
    "previous_visit_recommendations_fulfilled": false,
    "recommendations_commitments": "",
    "observations_visited": "",
    "objective": "",
    "visit_followup": "",
    "fulfilled_previous_recommendations": true,
    "new_recommendations": "",
    "observations_seg": "",
    "register_coinnovation": "",
    "local_practice_tool_technology_coinnovation_identified": true,
    "local_coinovation_or_technology_record": true,
    "name_innovation": "",
    "description_innovation": "",
    "problem_solution_innovation": "",
    "origin_and_developers": "",
    "materials_and_resources": "",
    "process_functioning": "",
    "potential_replication": "",
    "observations_extensionist": "",
    "date_hour_end": "",
    "socilization_next_event": "",
    "copy_documentation_delivered": false,
    "date_acompanamiento": "",
    "hour_acompanamiento": "",
    "origen_register": "MOBILE",
    "name_acompanamiento": "",
    "type_acompanamiento": "FOLLOW_UP",
    "other_acompanamiento": null,
    "visit_date": "",
    "attended_by": "",
    "user": "",
    "worker_up": "",
    "Household_size": "",
    "other": ""
  },
  "producter": {
    "identification": "",
    "name": "",
    "type_id": "",
    "number_phone": "",
    "is_woman_rural": false,
    "is_young_rural": false,
    "ethnic_belonging": "",
    "is_victim_conflict": false,
    "is_narp": false,
    "is_producer_organization_member": false,
    "organization_name": "",
    "representantive1_name": ""
  },
  "property": {
    "name": "",
    "latitude": "",
    "longitude": "",
    "asnm": "",
    "state": "",
    "city": "",
    "village": "",
    "linea_productive_primary": "",
    "linea_productive_secondary": "",
    "area_in_production": ""
  },
  "files": []
}



CURL PUT EXACTO (MISMO QUE POST PERO CON LA RUTA DINÁMICA)
Elimina nada / no agrega nada. Son exactamente los mismos campos del POST.
📌 Recuerda cambiar {survey_id} por el ID real a actualizar.
 
🚀 CURL PUT COMPLETO
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/1/{survey_id}' \
--header 'accept: application/json' \
--form 'api_key="63715a74a9a4073fe35bdf00f4b6f445ef32a67fe5b9b53554cc06bd64e60bd8"' \
--form 'survey_data="{
  \"medition_focalization\": {
    \"control_resources\": {
      \"obervation\": \"Notas sobre control de recursos\",
      \"score\": 4
    },
    \"voice_influence_decision\": {
      \"obervation\": \"Notas sobre voz e influencia\",
      \"score\": 3
    },
    \"leadership_innovation\": {
      \"obervation\": \"Notas sobre liderazgo\",
      \"score\": 5
    },
    \"dialogue_knowledge\": {
      \"obervation\": \"Notas sobre diálogo de saberes\",
      \"score\": 4
    }
  },
  \"classification_user\": {
    \"development_human_capacity\": {
      \"score\": 3,
      \"observation\": \"Notes on human capacity\"
    },
    \"development_social_capacity\": {
      \"score\": 2,
      \"observation\": \"Notes on social capacity\"
    },
    \"participation_public_political\": {
      \"score\": 2,
      \"observation\": \"Notes on political capacity\"
    },
    \"access_adaptative_adoption_information\": {
      \"score\": 4,
      \"observation\": \"Notes on productive capacity\"
    },
    \"sustainable_management_natural_resources\": {
      \"score\": 3,
      \"observation\": \"Notes on financial capacity\"
    }
  },
  \"objetive_accompaniment\": \"Objetivo del acompañamiento\",
  \"initial_diagnosis\": \"Diagnóstico inicial del predio\",
  \"recommendations_commitments\": \"Recomendaciones y compromisos adquiridos\",
  \"observations_visited\": \"Observaciones generales de la visita\",
  \"date_acompanamiento\": \"2025-11-21\",
  \"hour_acompanamiento\": \"10:30:00\",
  \"origen_register\": \"MOBILE\",
  \"name_acompanamiento\": \"Nombre del técnico\",
  \"visit_date\": \"2025-11-21T10:30:00\",
  \"attended_by\": \"Nombre de quien atiende\"
}"' \
--form 'producter_data="{
  \"identification\":\"123456789\",
  \"name\":\"John Doe\",
  \"type_id\":\"CC\",
  \"number_phone\":\"3001234567\",
  \"is_woman_rural\":false,
  \"is_young_rural\":true,
  \"ethnic_belonging\":\"None\",
  \"is_victim_conflict\":false,
  \"is_narp\":false,
  \"is_producer_organization_member\":true,
  \"organization_name\":\"ASOPROCAFE\",
  \"representantive1_name\":\"Jane Doe\"
}"' \
--form 'property_data="{
  \"name\":\"La Esperanza Farm\",
  \"latitude\":\"11.23\",
  \"longitude\":\"-74.20\",
  \"asnm\":\"100\",
  \"state\":\"Magdalena\",
  \"city\":\"Santa Marta\",
  \"village\":\"Minca\",
  \"linea_productive_primary\":\"Coffee\",
  \"linea_productive_secondary\":\"Avocado\",
  \"area_in_production\":\"40\"
}"' \
--form 'classification_user_data="{
  \"main_productive_activity\":1,
  \"secondary_productive_activities\":2,
  \"tools_and_equipment\":3,
  \"good_agricultural_practices\":1,
  \"commercialization_structure\":2,
  \"markets\":3,
  \"added_value\":1,
  \"records\":2,
  \"labor_type\":3,
  \"credit_and_banking\":1,
  \"organization_membership\":2,
  \"collective_activities\":3,
  \"entrepreneurship_associativity\":1,
  \"commercial_alliances\":2,
  \"technical_support\":3,
  \"quality_certifications\":1,
  \"intellectual_property\":2,
  \"access_information_sources\":3,
  \"access_to_ict\":1,
  \"use_of_ict_decision\":2,
  \"ict_skills\":3,
  \"knowledge_appropriation\":1,
  \"environmental_practices\":2,
  \"sustainable_practices\":3,
  \"climate_change_adaptation\":1,
  \"environmental_regulations\":2,
  \"participation_mechanisms\":3,
  \"participation_tools\":1,
  \"political_social_control\":2,
  \"community_self_management\":3
}"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"'





SURVEY 2

Endpoints de Survey 2
Asumiendo la misma estructura que mostraste para el survey 1, para survey 2 la API queda así:
Crear (POST)
POST /api/v1/surveys/2
Actualizar (PUT dinámico)
PUT /api/v1/surveys/2/{survey_id}
Donde {survey_id} es el ID de la encuesta que se quiere actualizar (por ejemplo, 4).
Los campos del PUT deben ser los mismos del POST (mismo nombre de campos en survey_data, producter_data, property_data), tal como me pediste.
La estructura del response es igual a la que ya tienes para los otros surveys, algo tipo:
{
  "data": {
    "id": 4,
    "state": "pending"
  },
  "message": "Survey 2 with ID 4 updated successfully and set to pending.",
  "success": true
}
(o al menos data, message, success con esa misma lógica).
 
🔹 2. CURL POST – Survey 2 (creación)
curl --location 'http://45.65.200.114:8000/api/v1/surveys/2' \
--header 'accept: application/json' \
--form 'api_key="63715a74a9a4073fe35bdf00f4b6f445ef32a67fe5b9b53554cc06bd64e60bd8"' \
--form 'survey_data="{
  \"objective_accompaniment\":\"Follow-up objective\",
  \"visit_development_follow_up_activities\":\"Activities for follow-up\",
  \"previous_visit_recommendations_fulfilled\":true,
  \"recommendations_commitments\":\"New recommendations\",
  \"observations_visited\":\"Observations from the visit\",
  \"objective\":\"Objective of the previous visit\",
  \"visit_followup\":\"Progress, difficulties, pending tasks\",
  \"fulfilled_previous_recommendations\":true,
  \"new_recommendations\":\"New recommendations based on follow-up\",
  \"observations_seg\":\"Follow-up observations\",
  \"register_coinnovation\":\"Co-innovation registration details\",
  \"local_practice_tool_technology_coinnovation_identified\":true,
  \"local_coinovation_or_technology_record\":true,
  \"name_innovation\":\"Drip Irrigation System\",
  \"description_innovation\":\"A locally adapted drip irrigation system.\",
  \"problem_solution_innovation\":\"Solves water scarcity during dry seasons.\",
  \"origin_and_developers\":\"Developed by local farmers.\",
  \"materials_and_resources\":\"Recycled plastic bottles, hoses.\",
  \"process_functioning\":\"Water is slowly released to the plant roots.\",
  \"potential_replication\":\"High potential for replication in the region.\",
  \"observations_extensionist\":\"The innovation is simple and effective.\",
  \"date_hour_end\":\"2025-11-08T12:00:00\",
  \"socilization_next_event\":\"Next event will be on...\",
  \"copy_documentation_delivered\":true,
  \"date_acompanamiento\":\"2025-11-08\",
  \"hour_acompanamiento\":\"11:00\",
  \"origen_register\":\"MOBILE\",
  \"name_acompanamiento\":\"Seguimiento 1\",
  \"type_acompanamiento\":\"FOLLOW_UP\",
  \"other_acompanamiento\":null,
  \"visit_date\":\"2025-11-08T11:00:00\",
  \"attended_by\":\"Jane Doe\",
  \"user\":\"Associated user\",
  \"worker_up\":\"UP Worker\",
  \"Household_size\":\"3\",
  \"other\":\"Other info\"
}"' \
--form 'producter_data="{
  \"identification\":\"123456789\",
  \"name\":\"John Doe\",
  \"type_id\":\"CC\",
  \"number_phone\":\"3001234567\",
  \"is_woman_rural\":false,
  \"is_young_rural\":true,
  \"ethnic_belonging\":\"None\",
  \"is_victim_conflict\":false,
  \"is_narp\":false,
  \"is_producer_organization_member\":true,
  \"organization_name\":\"ASOPROCAFE\",
  \"representantive1_name\":\"Jane Doe\"
}"' \
--form 'property_data="{
  \"name\":\"La Esperanza Farm\",
  \"latitude\":\"11.23\",
  \"longitude\":\"-74.20\",
  \"asnm\":\"100\",
  \"state\":\"Magdalena\",
  \"city\":\"Santa Marta\",
  \"village\":\"Minca\",
  \"linea_productive_primary\":\"Coffee\",
  \"linea_productive_secondary\":\"Avocado\",
  \"area_in_production\":\"40\"
}"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"'
 
🔹 3. CURL PUT – Survey 2 (actualización, mismos campos que el POST)
Ahora, el PUT con la misma estructura de campos del POST (tal como hicimos con survey 1).
Solo cambia:
•	El método: --request PUT
•	La URL: .../surveys/2/{survey_id}
Ejemplo usando survey_id = 4 (cámbialo según el ID real):
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/2/4' \
--header 'accept: application/json' \
--form 'api_key="63715a74a9a4073fe35bdf00f4b6f445ef32a67fe5b9b53554cc06bd64e60bd8"' \
--form 'survey_data="{
  \"objective_accompaniment\":\"Follow-up objective\",
  \"visit_development_follow_up_activities\":\"Activities for follow-up\",
  \"previous_visit_recommendations_fulfilled\":true,
  \"recommendations_commitments\":\"New recommendations\",
  \"observations_visited\":\"Observations from the visit\",
  \"objective\":\"Objective of the previous visit\",
  \"visit_followup\":\"Progress, difficulties, pending tasks\",
  \"fulfilled_previous_recommendations\":true,
  \"new_recommendations\":\"New recommendations based on follow-up\",
  \"observations_seg\":\"Follow-up observations\",
  \"register_coinnovation\":\"Co-innovation registration details\",
  \"local_practice_tool_technology_coinnovation_identified\":true,
  \"local_coinovation_or_technology_record\":true,
  \"name_innovation\":\"Drip Irrigation System\",
  \"description_innovation\":\"A locally adapted drip irrigation system.\",
  \"problem_solution_innovation\":\"Solves water scarcity during dry seasons.\",
  \"origin_and_developers\":\"Developed by local farmers.\",
  \"materials_and_resources\":\"Recycled plastic bottles, hoses.\",
  \"process_functioning\":\"Water is slowly released to the plant roots.\",
  \"potential_replication\":\"High potential for replication in the region.\",
  \"observations_extensionist\":\"The innovation is simple and effective.\",
  \"date_hour_end\":\"2025-11-08T12:00:00\",
  \"socilization_next_event\":\"Next event will be on...\",
  \"copy_documentation_delivered\":true,
  \"date_acompanamiento\":\"2025-11-08\",
  \"hour_acompanamiento\":\"11:00\",
  \"origen_register\":\"MOBILE\",
  \"name_acompanamiento\":\"Seguimiento 1\",
  \"type_acompanamiento\":\"FOLLOW_UP\",
  \"other_acompanamiento\":null,
  \"visit_date\":\"2025-11-08T11:00:00\",
  \"attended_by\":\"Jane Doe\",
  \"user\":\"Associated user\",
  \"worker_up\":\"UP Worker\",
  \"Household_size\":\"3\",
  \"other\":\"Other info\"
}"' \
--form 'producter_data="{
  \"identification\":\"123456789\",
  \"name\":\"John Doe\",
  \"type_id\":\"CC\",
  \"number_phone\":\"3001234567\",
  \"is_woman_rural\":false,
  \"is_young_rural\":true,
  \"ethnic_belonging\":\"None\",
  \"is_victim_conflict\":false,
  \"is_narp\":false,
  \"is_producer_organization_member\":true,
  \"organization_name\":\"ASOPROCAFE\",
  \"representantive1_name\":\"Jane Doe\"
}"' \
--form 'property_data="{
  \"name\":\"La Esperanza Farm\",
  \"latitude\":\"11.23\",
  \"longitude\":\"-74.20\",
  \"asnm\":\"100\",
  \"state\":\"Magdalena\",
  \"city\":\"Santa Marta\",
  \"village\":\"Minca\",
  \"linea_productive_primary\":\"Coffee\",
  \"linea_productive_secondary\":\"Avocado\",
  \"area_in_production\":\"40\"
}"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"'


SURVEY 3


Endpoints de Survey 3
•	Crear (POST)
POST http://45.65.200.114:8000/api/v1/surveys/3
•	Actualizar (PUT, dinámico)
PUT http://45.65.200.114:8000/api/v1/surveys/3/{survey_id}
Ejemplo: PUT http://45.65.200.114:8000/api/v1/surveys/3/5
En ambos casos se envía multipart/form-data con los mismos campos:
•	api_key
•	survey_data (JSON string)
•	producter_data (JSON string)
•	property_data (JSON string)
•	classification_user_data (JSON string)
•	files (opcional, repetible)
 
🔹 2. CURL POST – Survey 3 (creación)
curl --location 'http://45.65.200.114:8000/api/v1/surveys/3' \
--header 'accept: application/json' \
--form 'api_key="63715a74a9a4073fe35bdf00f4b6f445ef32a67fe5b9b53554cc06bd64e60bd8"' \
--form 'survey_data="{
  \"classification_user\": {
    \"development_human_capacity\": {
      \"observation\": \"Final notes on human capacity\",
      \"score\": 4
    },
    \"development_social_capacity\": {
      \"observation\": \"Final notes on social capacity\",
      \"score\": 3
    },
    \"access_adaptative_adoption_information\": {
      \"observation\": \"Final notes on productive capacity\",
      \"score\": 5
    },
    \"sustainable_management_natural_resources\": {
      \"observation\": \"Final notes on financial capacity\",
      \"score\": 4
    },
    \"participation_public_political\": {
      \"observation\": \"Final notes on political capacity\",
      \"score\": 3
    }
  },
  \"medition_focalization\": {
    \"control_resources\": {
      \"obervation\": \"Final notes on resource control\",
      \"score\": 5
    },
    \"voice_influence_decision\": {
      \"obervation\": \"Final notes on voice influence decision\",
      \"score\": 4
    },
    \"leadership_innovation\": {
      \"obervation\": \"Final notes on leadership innovation\",
      \"score\": 5
    },
    \"dialogue_knowledge\": {
      \"obervation\": \"Final notes on dialogue knowledge\",
      \"score\": 4
    }
  },
  \"objetive_accompaniment\": \"Final visit objective\",
  \"development_accompaniment\": \"Development of the final accompaniment.\",
  \"final_diagnosis\": \"Final diagnosis of the property.\",
  \"recommendations_commitments\": \"Final recommendations and commitments.\",
  \"observations_visited\": \"Final observations from the visit.\",
  \"date_hour_end\": \"2025-11-09T13:00:00\",
  \"copy_documentation_delivered\": \"true\",
  \"socialization_events_group\": \"Socialization of results with the producer group.\",
  \"not_agend_new_visit\": \"No new visit is scheduled as this is the final one.\",
  \"date_acompanamiento\": \"2025-11-09\",
  \"hour_acompanamiento\": \"12:00\",
  \"origen_register\": \"WEB\",
  \"name_acompanamiento\": \"Diagnóstico Final\",
  \"type_acompanamiento\": \"FINAL\",
  \"other_acompanamiento\": null,
  \"visit_date\": \"2025-11-09T12:00:00\",
  \"attended_by\": \"John Smith\",
  \"user\": \"Associated user\",
  \"worker_up\": \"UP Worker\",
  \"household_size\": \"5\",
  \"other\": \"Final notes\"
}"' \
--form 'producter_data="{
  \"identification\":\"123456789\",
  \"name\":\"John Doe\",
  \"type_id\":\"CC\",
  \"number_phone\":\"3001234567\",
  \"is_woman_rural\":false,
  \"is_young_rural\":true,
  \"ethnic_belonging\":\"None\",
  \"is_victim_conflict\":false,
  \"is_narp\":false,
  \"is_producer_organization_member\":true,
  \"organization_name\":\"ASOPROCAFE\",
  \"representantive1_name\":\"Jane Doe\"
}"' \
--form 'property_data="{
  \"name\":\"La Esperanza Farm\",
  \"latitude\":\"11.23\",
  \"longitude\":\"-74.20\",
  \"asnm\":\"100\",
  \"state\":\"Magdalena\",
  \"city\":\"Santa Marta\",
  \"village\":\"Minca\",
  \"linea_productive_primary\":\"Coffee\",
  \"linea_productive_secondary\":\"Avocado\",
  \"area_in_production\":\"40\"
}"' \
--form 'classification_user_data="{
  \"main_productive_activity\":1,
  \"secondary_productive_activities\":2,
  \"tools_and_equipment\":3,
  \"good_agricultural_practices\":1,
  \"commercialization_structure\":2,
  \"markets\":3,
  \"added_value\":1,
  \"records\":2,
  \"labor_type\":3,
  \"credit_and_banking\":1,
  \"organization_membership\":2,
  \"collective_activities\":3,
  \"entrepreneurship_associativity\":1,
  \"commercial_alliances\":2,
  \"technical_support\":3,
  \"quality_certifications\":1,
  \"intellectual_property\":2,
  \"access_information_sources\":3,
  \"access_to_ict\":1,
  \"use_of_ict_decision\":2,
  \"ict_skills\":3,
  \"knowledge_appropriation\":1,
  \"environmental_practices\":2,
  \"sustainable_practices\":3,
  \"climate_change_adaptation\":1,
  \"environmental_regulations\":2,
  \"participation_mechanisms\":3,
  \"participation_tools\":1,
  \"political_social_control\":2,
  \"community_self_management\":3
}"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"' \
--form 'files=@"/Users/alex_espinosa/Downloads/photo.jpg"'
 
🔹 3. CURL PUT – Survey 3 (actualización, mismos campos que el POST)
Ahora el PUT corregido, con la misma estructura de campos que el POST (no reducido como en tu ejemplo, sino completo).
Solo cambia:
•	Método: --request PUT
•	URL: .../surveys/3/{survey_id} (ejemplo: /3/5)
•	Puedes usar la misma api_key que en el POST (o la que corresponda realmente).
curl --location --request PUT 'http://45.65.200.114:8000/api/v1/surveys/3/5' \
--header 'accept: application/json' \
--form 'api_key="63715a74a9a4073fe5b9b53554cc06bd64e60bd8"' \
--form 'survey_data="{
  \"classification_user\": {
    \"development_human_capacity\": {
      \"observation\": \"Final notes on human capacity\",
      \"score\": 4
    },
    \"development_social_capacity\": {
      \"observation\": \"Final notes on social capacity\",
      \"score\": 3
    },
    \"access_adaptative_adoption_information\": {
      \"observation\": \"Final notes on productive capacity\",
      \"score\": 5
    },
    \"sustainable_management_natural_resources\": {
      \"observation\": \"Final notes on financial capacity\",
      \"score\": 4
    },
    \"participation_public_political\": {
      \"observation\": \"Final notes on political capacity\",
      \"score\": 3
    }
  },
  \"medition_focalization\": {
    \"control_resources\": {
      \"obervation\": \"Final notes on resource control\",
      \"score\": 5
    },
    \"voice_influence_decision\": {
      \"obervation\": \"Final notes on voice influence decision\",
      \"score\": 4
    },
    \"leadership_innovation\": {
      \"obervation\": \"Final notes on leadership innovation\",
      \"score\": 5
    },
    \"dialogue_knowledge\": {
      \"obervation\": \"Final notes on dialogue knowledge\",
      \"score\": 4
    }
  },
  \"objetive_accompaniment\": \"Final visit objective\",
  \"development_accompaniment\": \"Development of the final accompaniment.\",
  \"final_diagnosis\": \"Final diagnosis of the property.\",
  \"recommendations_commitments\": \"Final recommendations and commitments.\",
  \"observations_visited\": \"Final observations from the visit.\",
  \"date_hour_end\": \"2025-11-09T13:00:00\",
  \"copy_documentation_delivered\": \"true\",
  \"socialization_events_group\": \"Socialization of results with the producer group.\",
  \"not_agend_new_visit\": \"No new visit is scheduled as this is the final one.\",
  \"date_acompanamiento\": \"2025-11-09\",
  \"hour_acompanamiento\": \"12:00\",
  \"origen_register\": \"WEB\",
  \"name_acompanamiento\": \"Diagnóstico Final\",
  \"type_acompanamiento\": \"FINAL\",
  \"other_acompanamiento\": null,
  \"visit_date\": \"2025-11-09T12:00:00\",
  \"attended_by\": \"John Smith\",
  \"user\": \"Associated user\",
  \"worker_up\": \"UP Worker\",
  \"household_size\": \"5\",
  \"other\": \"Final notes\"
}"' \
--form 'producter_data="{
  \"identification\":\"123456789\",
  \"name\":\"John Doe\",
  \"type_id\":\"CC\",
  \"number_phone\":\"3001234567\",
  \"is_woman_rural\":false,
  \"is_young_rural\":true,
  \"ethnic_belonging\":\"None\",
  \"is_victim_conflict\":false,
  \"is_narp\":false,
  \"is_producer_organization_member\":true,
  \"organization_name\":\"ASOPROCAFE\",
  \"representantive1_name\":\"Jane Doe\"
}"' \
--form 'property_data="{
  \"name\":\"La Esperanza Farm\",
  \"latitude\":\"11.23\",
  \"longitude\":\"-74.20\",
  \"asnm\":\"100\",
  \"state\":\"Magdalena\",
  \"city\":\"Santa Marta\",
  \"village\":\"Minca\",
  \"linea_productive_primary\":\"Coffee\",
  \"linea_productive_secondary\":\"Avocado\",
  \"area_in_production\":\"40\"
}"' \"' \
--form 'files=@"/path/to/photo_user.jpg"' \
--form 'files=@"/path/to/photo_interaction.jpg"' \
--form 'files=@"/path/to/photo_panorama.jpg"' \
--form 'files=@"/path/to/photo_extra.jpg"'

