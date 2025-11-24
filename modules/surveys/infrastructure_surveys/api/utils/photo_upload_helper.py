import os
import shutil
import uuid
from typing import Optional

from fastapi import UploadFile

from modules.surveys.application_surveys.dtos.photo_paths_dto import (
    SurveyPhotoPathsDTO,
)

UPLOAD_DIRECTORY = "./uploads"


def _ensure_upload_directory() -> None:
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


def _save_single_file(file: UploadFile) -> str:
    _ensure_upload_directory()
    _, extension = os.path.splitext(file.filename or "")
    unique_filename = f"{uuid.uuid4()}{extension}"
    file_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_path


def _save_optional_file(file: Optional[UploadFile]) -> Optional[str]:
    if file is None:
        return None
    return _save_single_file(file)


def save_required_photo_files(
    photo_user: UploadFile,
    photo_interaction: UploadFile,
    photo_panorama: UploadFile,
    phono_extra_1: Optional[UploadFile] = None,
) -> SurveyPhotoPathsDTO:
    photos = SurveyPhotoPathsDTO(
        photo_user=_save_single_file(photo_user),
        photo_interaction=_save_single_file(photo_interaction),
        photo_panorama=_save_single_file(photo_panorama),
        phono_extra_1=_save_optional_file(phono_extra_1),
    )
    photos.ensure_required()
    return photos


def save_optional_photo_files(
    photo_user: Optional[UploadFile] = None,
    photo_interaction: Optional[UploadFile] = None,
    photo_panorama: Optional[UploadFile] = None,
    phono_extra_1: Optional[UploadFile] = None,
) -> Optional[SurveyPhotoPathsDTO]:
    photos = SurveyPhotoPathsDTO(
        photo_user=_save_optional_file(photo_user),
        photo_interaction=_save_optional_file(photo_interaction),
        photo_panorama=_save_optional_file(photo_panorama),
        phono_extra_1=_save_optional_file(phono_extra_1),
    )
    return photos if photos.has_updates() else None
