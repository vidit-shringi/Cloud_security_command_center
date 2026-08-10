"""
Core validation utilities for inputs and AWS structures.
Ensures protection against injection or malformed data.
"""
import re
from core.exceptions import InternShieldBaseError

def validate_aws_region(region: str) -> bool:
    """Validates if a string matches standard AWS region formats."""
    # Matches patterns like us-east-1, eu-central-1, ap-northeast-2
    pattern = r"^[a-z]{2}-[a-z]+-\d+$"
    return bool(re.match(pattern, region))

def validate_docker_image_name(image_name: str) -> bool:
    """Validates Docker image names to prevent shell injection."""
    # Allows standard alphanumeric, dashes, underscores, slashes, and tags
    pattern = r"^([a-zA-Z0-9_\-\./]+)(:[a-zA-Z0-9_\-\.]+)?$"
    if not re.match(pattern, image_name):
        raise InternShieldBaseError(f"Invalid Docker image format: {image_name}")
    return True