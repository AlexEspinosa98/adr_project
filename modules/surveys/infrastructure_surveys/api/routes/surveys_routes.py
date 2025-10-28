from logging import Logger
from fastapi import APIRouter, Depends, HTTPException, status as response_status, File, UploadFile, Form, Body, Query
from typing import List, Optional, Union
from datetime import datetime
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
from modules.surveys.application_surveys.dtos.input_dto.create_survey2_input_dto import CreateSurvey2InputDTO
from modules.surveys.application_surveys.dtos.output_dto.create_survey2_output_dto import CreateSurvey2OutputDTO
from modules.surveys.application_surveys.services.survey2_service import Survey2Service
from modules.surveys.infrastructure_surveys.services.survey2_service_composer import get_survey2_service
from modules.surveys.application_surveys.services.list_surveys_service import ListSurveysService
from modules.surveys.infrastructure_surveys.services.list_surveys_service_composer import get_list_surveys_service
from modules.surveys.application_surveys.dtos.output_dto.survey_list_item_dto import SurveyListItemDTO
from common.application.dtos.input_dto.pagination_dto import PaginationInputDTO
from common.infrastructure.api.dependencies.pagination_dependencies import get_pagination_params
from common.infrastructure.api.dtos.pagination_response_dto import PaginatedApiResponseDTO

from common.infrastructure.api.dtos.response_dto import ApiResponseDTO
from common.infrastructure.logging.config import get_logger

from fastapi import Depends, status, HTTPException
from common.infrastructure.api.dtos.response_dto import ApiResponseDTO
from common.infrastructure.authentication.user_authorizer import get_current_user
from common.application.dtos.output_dto.authentication_dto import AuthenticatedUserDTO
from common.infrastructure.database.session import session_manager
from sqlalchemy.orm import Session
from modules.surveys.application_surveys.use_cases.update_survey_state import UpdateSurveyState
from modules.surveys.application_surveys.dtos.input_dto.update_survey_state_input_dto import UpdateSurveyStateInputDTO

from modules.surveys.application_surveys.services.get_survey_detail_service import GetSurveyDetailService
from modules.surveys.infrastructure_surveys.services.get_survey_detail_service_composer import get_survey_detail_service
from modules.surveys.application_surveys.dtos.output_dto.survey1_detail_output_dto import Survey1DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey2_detail_output_dto import Survey2DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey3_detail_output_dto import Survey3DetailOutputDTO

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

        survey_data_dict['classification_user'] = classification_user_data_dict

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


@router.post("/2", status_code=response_status.HTTP_201_CREATED)
async def create_survey2(
    api_key: str = Form(...),
    survey_data: str = Form(...),
    producter_data: str = Form(...),
    property_data: str = Form(...),
    files: List[UploadFile] = File(...),
    survey_service: Survey2Service = Depends(get_survey2_service),
) -> ApiResponseDTO[CreateSurvey2OutputDTO]:
    _LOGGER.info(f"Creating new survey 2")
    
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

        producter_input_dto = SurveyUserProducterInputDTO(**producter_data_dict)
        property_info_input_dto = PropertyInfoInputDTO(**property_data_dict)

        input_dto = CreateSurvey2InputDTO(
            **survey_data_dict
        )
        result = survey_service.create_survey2(input_dto, producter_input_dto, property_info_input_dto, api_key, image_paths)
    except Exception as e:
        _LOGGER.error(f"Error creating survey 2: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error creating survey 2.")
    
    return ApiResponseDTO.success_response(
        data=result,
        message="Survey 2 created successfully"
    )


@router.post("/3", status_code=response_status.HTTP_201_CREATED)
async def create_survey3(
    api_key: str = Form(...),
    survey_data: str = Form(...),
    producter_data: str = Form(...),
    property_data: str = Form(...),
    classification_user_data: str = Form(...),
    files: List[UploadFile] = File(...),
    survey_service: Survey3Service = Depends(get_survey3_service),
) -> ApiResponseDTO[CreateSurvey3OutputDTO]:
    _LOGGER.info(f"Creating new survey 3")
    
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

        survey_data_dict['classification_user'] = classification_user_data_dict

        producter_input_dto = SurveyUserProducterInputDTO(**producter_data_dict)
        property_info_input_dto = PropertyInfoInputDTO(**property_data_dict)
        classification_user_input_dto = ClassificationUserInputDTO(**classification_user_data_dict)

        input_dto = CreateSurvey3InputDTO(
            **survey_data_dict
        )
        result = survey_service.create_survey3(input_dto, producter_input_dto, property_info_input_dto, classification_user_input_dto, api_key, image_paths)
    except Exception as e:
        _LOGGER.error(f"Error creating survey 3: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error creating survey 3.")
    
    return ApiResponseDTO.success_response(
        data=result,
        message="Survey 3 created successfully"
    )


@router.get("", response_model=PaginatedApiResponseDTO[SurveyListItemDTO])
async def list_surveys(
    pagination: PaginationInputDTO = Depends(get_pagination_params),
    api_key: Optional[str] = Query(None),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    farm_name: Optional[str] = None,
    survey_type: Optional[int] = None,
    list_surveys_service: ListSurveysService = Depends(get_list_surveys_service),
):
    paginated_result = list_surveys_service.list_surveys(
        pagination=pagination,
        api_key=api_key,
        start_date=start_date,
        end_date=end_date,
        farm_name=farm_name,
        survey_type=survey_type,
    )
    return PaginatedApiResponseDTO.create_paginated_success(
        items=paginated_result.items,
        pagination_input=pagination,
        total_items=paginated_result.pagination.total_items,
        message="Surveys retrieved successfully",
    )


@router.get("/{survey_type}/{survey_id}", response_model=ApiResponseDTO[Union[Survey1DetailOutputDTO, Survey2DetailOutputDTO, Survey3DetailOutputDTO]])
async def get_survey_detail(
    survey_type: int,
    survey_id: int,
    survey_detail_service: GetSurveyDetailService = Depends(get_survey_detail_service),
) -> ApiResponseDTO[Union[Survey1DetailOutputDTO, Survey2DetailOutputDTO, Survey3DetailOutputDTO]]:
    _LOGGER.info(f"Fetching detail for survey type {survey_type} with ID {survey_id}")
    
    survey_detail = survey_detail_service.get_survey_detail(survey_id, survey_type)
    
    if not survey_detail:
        raise HTTPException(status_code=response_status.HTTP_404_NOT_FOUND, detail="Survey not found")
        
    return ApiResponseDTO.success_response(
        data=survey_detail,
        message=f"Survey type {survey_type} with ID {survey_id} retrieved successfully"
    )



