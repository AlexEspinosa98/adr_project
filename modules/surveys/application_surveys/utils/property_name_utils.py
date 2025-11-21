import re
from typing import Optional


def normalize_property_name(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None

    cleaned = value.strip()
    if not cleaned:
        return None

    # Replace all non-alphanumeric characters with a space, collapse spaces, then snake_case.
    cleaned = re.sub(r"[^0-9a-zA-Z]+", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip().lower()
    return cleaned.replace(" ", "_")


def denormalize_property_name(value: Optional[str]) -> Optional[str]:
    if not value:
        return value

    words = value.replace("_", " ").split()
    return " ".join(word.capitalize() for word in words)
