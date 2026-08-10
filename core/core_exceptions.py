"""
Core exceptions for the InternShield CSCC.
Provides structured error handling across all modules.
"""

class InternShieldBaseError(Exception):
    """Base exception for all InternShield errors."""
    pass

class ConfigurationError(InternShieldBaseError):
    """Raised when there is an issue with config.yaml or .env."""
    pass

class AWSAccessError(InternShieldBaseError):
    """Raised when AWS credentials or permissions are insufficient."""
    pass

class ToolMissingError(InternShieldBaseError):
    """Raised when an external CLI tool (like Trivy or AWS CLI) is missing."""
    pass

class AIProviderError(InternShieldBaseError):
    """Raised when an AI Provider fails to respond or authenticate."""
    pass

class AssessmentError(InternShieldBaseError):
    """Raised when a specific security module fails its execution."""
    pass