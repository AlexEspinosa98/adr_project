from dataclasses import dataclass
from typing import Optional


@dataclass
class SurveyPhotoPathsDTO:
    """
    Simple DTO used to keep the photo paths aligned with their semantic meaning.
    """

    photo_user: Optional[str] = None
    photo_interaction: Optional[str] = None
    photo_panorama: Optional[str] = None
    phono_extra_1: Optional[str] = None

    def has_updates(self) -> bool:
        return any(
            [
                self.photo_user is not None,
                self.photo_interaction is not None,
                self.photo_panorama is not None,
                self.phono_extra_1 is not None,
            ]
        )

    def ensure_required(self) -> None:
        missing = [
            name
            for name, value in (
                ("photo_user", self.photo_user),
                ("photo_interaction", self.photo_interaction),
                ("photo_panorama", self.photo_panorama),
            )
            if not value
        ]
        if missing:
            raise ValueError(
                f"Missing required photos: {', '.join(missing)}"
            )
