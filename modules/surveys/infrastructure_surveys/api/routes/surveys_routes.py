from logging import Logger
from fastapi import APIRouter, Depends, HTTPException, status as response_status, File, UploadFile, Form, Body
from typing import List
import json
import shutil
import os

from modules.surveys.application_surveys.dtos.input_dto.create_survey1_input_dto import CreateSurvey1InputDTO
from modules.surveys.application_surveys.dtos.output_dto.create_survey1_output_dto import CreateSurvey1OutputDTO
from modules.surveys.application_surveys.services.survey1_service import Survey1Service
from modules.surveys.infrastructure_surveys.services.survey1_service_composer import get_survey1_service
from modules.surveys.application_surveys.dtos.input_dto.survey_user_producter import SurveyUserProducterInputDTO
from modules.surveys.application_surveys.dtos.input_dto.property_info_input_dto import PropertyInfoInputDTO
from modules.surveys.application_surveys.dtos.input_dto.classification_user_input_dto import ClassificationUserInputDTO


from modules.surveys.application_surveys.dtos.input_dto.create_survey3_input_dto import CreateSurvey3InputDTO
from modules.surveys.application_surveys.dtos.output_dto.create_survey3_output_dto import CreateSurvey3OutputDTO
from modules.surveys.application_surveys.services.survey3_service import Survey3Service
from modules.surveys.infrastructure_surveys.services.survey3_service_composer import get_survey3_service

from common.infrastructure.api.dtos.response_dto import ApiResponseDTO
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

router = APIRouter(prefix="/surveys", tags=["surveys"])

UPLOAD_DIRECTORY = "./uploads"

@router.post("/1", status_code=response_status.HTTP_201_CREATED)
async def create_survey1(
    api_key: str = Form(...),
    survey_data: str = Form(...),
    producter_data: str = Form(...),
    property_data: str = Form(...),
    classification_user_data: str = Form(...),
    files: List[UploadFile] = File(...),
    survey_service: Survey1Service = Depends(get_survey1_service),
) -> ApiResponseDTO[CreateSurvey1OutputDTO]:
    _LOGGER.info(f"Creating new survey 1")
    
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    image_paths = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        image_paths.append(file_path)

    try:
        survey_data_dict = json.loads(survey_data)
        producter_data_dict = json.loads(producter_data)
        property_data_dict = json.loads(property_data)
        classification_user_data_dict = json.loads(classification_user_data)

        producter_input_dto = SurveyUserProducterInputDTO(**producter_data_dict)
        property_info_input_dto = PropertyInfoInputDTO(**property_data_dict)
        classification_user_input_dto = ClassificationUserInputDTO(**classification_user_data_dict)

        input_dto = CreateSurvey1InputDTO(
            **survey_data_dict
        )
        result = survey_service.create_survey1(input_dto, producter_input_dto, property_info_input_dto, classification_user_input_dto, api_key, image_paths)
    except Exception as e:
        _LOGGER.error(f"Error creating survey 1: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error creating survey 1.")
    
    return ApiResponseDTO.success_response(
        data=result,
        message="Survey 1 created successfully"
    )
