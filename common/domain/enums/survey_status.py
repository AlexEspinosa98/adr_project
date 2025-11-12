from enum import Enum


class SurveyStatus(str, Enum):
    PENDING = "pending"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
