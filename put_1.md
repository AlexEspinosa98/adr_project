# PUT /surveys/1/{survey_id}

Edit an existing Survey 1. The survey must currently be `rejected`; after a successful update it is set back to `pending`.

## Request
- **Method:** `PUT`
- **Path:** `/surveys/1/{survey_id}`
- **Content-Type:** `multipart/form-data`

| Form Field | Type | Required | Description |
|------------|------|----------|-------------|
| `api_key` | `string` | Yes | API key of the extensionist editing the survey. |
| `survey_data` | `string` (JSON) | Yes | Fields that map to `UpdateSurvey1InputDTO`. |
| `producter_data` | `string` (JSON) | Yes | Same shape used on POST `/surveys/1`. |
| `property_data` | `string` (JSON) | Yes | Same shape used on POST `/surveys/1`. |
| `files` | `List[UploadFile]` | No | Up to 4 replacement images in the order: user, interaction, panorama, extra. |

> `classification_user_data` is **not** sent in this endpoint.

### Example `survey_data`
```json
{
  "objetive_accompaniment": "Objective of the visit",
  "initial_diagnosis": "Initial diagnosis of the property",
  "recommendations_commitments": "Recommendations and commitments",
  "observations_visited": "Observations from the visit",
  "visit_date": "2025-11-07T10:00:00Z",
  "attended_by": "Name of the person attended",
  "user": "Associated user",
  "worker_up": "UP Worker",
  "other": "Other relevant information",
  "copy_documentation_delivered": null,
  "date_hour_end": null,
  "date_acompanamiento": "2025-11-07T00:00:00",
  "origen_register": "MOBILE",
  "name_acompanamiento": "pepito",
  "type_acompanamiento": "INITIAL",
  "other_acompanamiento": "nose",
  "household_size": "4"
}
```

### Example `producter_data`
```json
{
  "id": 2,
  "name": "John Doe",
  "type_id": "1",
  "identification": "123456789",
  "number_phone": null,
  "is_woman_rural": false,
  "is_young_rural": true,
  "ethnic_belonging": "None",
  "is_victim_conflict": false,
  "is_narp": false,
  "is_producer_organization_member": null,
  "organization_name": null,
  "representantive1_name": null
}
```

### Example `property_data`
```json
{
  "id": 2,
  "name": "La Esperanza Farm",
  "latitude": "11.23",
  "longitude": "-74.20",
  "asnm": "100",
  "state": "Magdalena",
  "city": "Santa Marta",
  "village": "Minca",
  "total_area": null,
  "linea_productive_primary": "Coffee",
  "area_total_linea_productive_primary": null,
  "linea_productive_secondary": "Avocado",
  "area_total_linea_productive_secondary": null,
  "area_in_production": "40"
}
```

## Example cURL
```bash
curl -X PUT "https://api.example.com/surveys/1/17" \
  -H "Content-Type: multipart/form-data" \
  -F 'api_key=EXT-123' \
  -F 'survey_data={
        "objetive_accompaniment": "Objective of the visit",
        "initial_diagnosis": "Initial diagnosis of the property",
        "recommendations_commitments": "Recommendations and commitments",
        "observations_visited": "Observations from the visit",
        "visit_date": "2025-11-07T10:00:00Z",
        "attended_by": "Name of the person attended",
        "user": "Associated user",
        "worker_up": "UP Worker",
        "other": "Other relevant information",
        "copy_documentation_delivered": null,
        "date_hour_end": null,
        "date_acompanamiento": "2025-11-07T00:00:00",
        "origen_register": "MOBILE",
        "name_acompanamiento": "pepito",
        "type_acompanamiento": "INITIAL",
        "other_acompanamiento": "nose",
        "household_size": "4"
      }' \
  -F 'producter_data={
        "id": 2,
        "name": "John Doe",
        "type_id": "1",
        "identification": "123456789",
        "number_phone": null,
        "is_woman_rural": false,
        "is_young_rural": true,
        "ethnic_belonging": "None",
        "is_victim_conflict": false,
        "is_narp": false,
        "is_producer_organization_member": null,
        "organization_name": null,
        "representantive1_name": null
      }' \
  -F 'property_data={
        "id": 2,
        "name": "La Esperanza Farm",
        "latitude": "11.23",
        "longitude": "-74.20",
        "asnm": "100",
        "state": "Magdalena",
        "city": "Santa Marta",
        "village": "Minca",
        "total_area": null,
        "linea_productive_primary": "Coffee",
        "area_total_linea_productive_primary": null,
        "linea_productive_secondary": "Avocado",
        "area_total_linea_productive_secondary": null,
        "area_in_production": "40"
      }' \
  -F 'files=@/path/to/photo_user.jpg' \
  -F 'files=@/path/to/photo_interaction.jpg' \
  -F 'files=@/path/to/photo_panorama.jpg' \
  -F 'files=@/path/to/photo_extra.jpg'
```
