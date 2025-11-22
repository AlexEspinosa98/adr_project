# Documentación de la Encuesta Tipo 2

Este documento contiene los `curl` para crear (POST) y actualizar (PUT) la Encuesta Tipo 2, junto con las estructuras JSON esperadas.

**Nota Importante:** A diferencia de las encuestas 1 y 3, la encuesta 2 no maneja el campo `classification_user`.

---

## 1. Crear Encuesta (POST)

Este endpoint permite crear una nueva encuesta tipo 2 (Seguimiento y Co-Innovación). La petición debe ser de tipo `multipart/form-data`.

**Endpoint:** `POST /api/v1/surveys/2`

### Comando `curl` completo (auto-contenido)

```bash
curl --location 'http://127.0.0.1:8000/api/v1/surveys/2' \
--header 'accept: application/json' \
--form 'api_key="tu_api_key_aqui"' \
--form 'survey_data={
    "objective_accompaniment": "Seguimiento de actividades y compromisos",
    "visit_development_follow_up_activities": "Se revisaron los avances en la implementación de las camas de siembra.",
    "previous_visit_recommendations_fulfilled": true,
    "recommendations_commitments": "Continuar con el plan de fertilización y registrar resultados.",
    "observations_visited": "El productor muestra gran interés y ha aplicado las recomendaciones.",
    "name_innovation": "Sistema de riego por goteo artesanal",
    "description_innovation": "Uso de botellas plásticas para crear un sistema de riego localizado.",
    "problem_solution_innovation": "Reduce el consumo de agua y asegura humedad constante en las raíces.",
    "date_acompanamiento": "2025-11-22",
    "hour_acompanamiento": "09:00:00",
    "origen_register": "MOBILE",
    "name_acompanamiento": "Nombre del Técnico"
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
--form 'files=@"/ruta/a/tu/foto_seguimiento.jpg"' \
--form 'files=@"/ruta/a/tu/foto_innovacion.jpg"'
```

---

## 2. Actualizar Encuesta (PUT)

Este endpoint permite actualizar una encuesta tipo 2 existente. La petición debe ser de tipo `multipart/form-data`.

**Endpoint:** `PUT /api/v1/surveys/2/{survey_id}`

### Comando `curl` completo (auto-contenido)

```bash
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/surveys/2/1' \
--header 'accept: application/json' \
--form 'api_key="tu_api_key_aqui"' \
--form 'survey_data={
    "objective_accompaniment": "Ajuste del plan de seguimiento",
    "recommendations_commitments": "Se ajusta el plan de fertilización basado en los últimos resultados. Nueva recomendación: aplicar compostaje.",
    "observations_visited": "Se observa una mejora notable en la salud del cultivo."
}' \
--form 'producter_data={
    "identification": "123456789",
    "name": "John Doe Productor",
    "number_phone": "3007654321"
}' \
--form 'property_data={
    "name": "Finca La Esperanza",
    "area_in_production": "55"
}' \
--form 'files=@"/ruta/a/tu/nueva_foto.jpg"'
```
