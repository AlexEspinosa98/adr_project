# Documentación de la Encuesta Tipo 3

Este documento contiene los `curl` para crear (POST) y actualizar (PUT) la Encuesta Tipo 3 (Diagnóstico Final), junto con las estructuras JSON esperadas.

---

## 1. Crear Encuesta (POST)

Este endpoint permite crear una nueva encuesta tipo 3. La petición debe ser de tipo `multipart/form-data`.

**Endpoint:** `POST /api/v1/surveys/3`

### Comando `curl` completo (auto-contenido)

```bash
curl --location 'http://127.0.0.1:8000/api/v1/surveys/3' \
--header 'accept: application/json' \
--form 'api_key="tu_api_key_aqui"' \
--form 'survey_data={
    "medition_focalization": {
        "control_resources": {"obervation": "Notas finales sobre control de recursos", "score": 5},
        "voice_influence_decision": {"obervation": "Notas finales sobre voz e influencia", "score": 4},
        "leadership_innovation": {"obervation": "Notas finales sobre liderazgo", "score": 5},
        "dialogue_knowledge": {"obervation": "Notas finales sobre diálogo de saberes", "score": 5}
    },
    "objetive_accompaniment": "Cierre y diagnóstico final del ciclo de acompañamiento.",
    "development_accompaniment": "Se realizó un recorrido final por el predio, verificando la implementación de todas las recomendaciones.",
    "final_diagnosis": "El productor ha mejorado significativamente sus capacidades productivas y de gestión.",
    "recommendations_commitments": "Mantener las buenas prácticas y explorar nuevos mercados.",
    "observations_visited": "Se evidencia una excelente apropiación de las tecnologías y conocimientos compartidos.",
    "socialization_events_group": "Se invita al productor a participar en el evento de socialización de resultados el próximo mes.",
    "date_acompanamiento": "2025-11-22",
    "hour_acompanamiento": "15:00:00",
    "origen_register": "WEB",
    "name_acompanamiento": "Nombre del Técnico"
}' \
--form 'producter_data={
    "identification": "123456789",
    "name": "John Doe Productor",
    "type_id": "CC",
    "number_phone": "3001234567"
}' \
--form 'property_data={
    "name": "Finca La Esperanza",
    "latitude": "11.2345",
    "longitude": "-74.2012",
    "state": "Magdalena",
    "city": "Santa Marta"
}' \
--form 'classification_user_data={
    "main_productive_activity": 3,
    "secondary_productive_activities": 3,
    "tools_and_equipment": 2,
    "good_agricultural_practices": 1,
    "commercialization_structure": 2,
    "markets": 1,
    "added_value": 2,
    "records": 1,
    "labor_type": 3,
    "credit_and_banking": 2
}' \
--form 'files="/ruta/a/tu/foto_final1.jpg"' \
--form 'files="/ruta/a/tu/foto_final2.jpg"'
```

---

## 2. Actualizar Encuesta (PUT)

Este endpoint permite actualizar una encuesta tipo 3 existente. La petición debe ser de tipo `multipart/form-data` y el ID de la encuesta debe ir en el cuerpo del JSON `survey_data`.

**Endpoint:** `PUT /api/v1/surveys/3`

### Comando `curl` completo (auto-contenido)

```bash
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/surveys/3' \
--header 'accept: application/json' \
--form 'api_key="tu_api_key_aqui"' \
--form 'survey_data={
    "id": 3,
    "final_diagnosis": "Diagnóstico final actualizado: Se confirma la sostenibilidad del modelo productivo.",
    "observations_visited": "Observaciones actualizadas: El productor ha comenzado a enseñar las prácticas a sus vecinos.",
    "classification_user": {
      "main_productive_activity": 1,
      "secondary_productive_activities": 1
    }
}' \
--form 'producter_data={
    "identification": "123456789",
    "name": "John Doe Productor Final"
}' \
--form 'property_data={
    "name": "Finca La Esperanza Próspera"
}' \
--form 'files="/ruta/a/tu/foto_actualizada.jpg"'
```
