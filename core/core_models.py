"""
Data models for the InternShield CSCC.
Uses Pydantic for strict data validation and normalization of findings.
"""
from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone

class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"

class Finding(BaseModel):
    """Centralized model for all security findings."""
    finding_id: str = Field(..., description="Unique ID for the finding (e.g., S3-001)")
    title: str = Field(..., description="Short, descriptive title")
    category: str = Field(..., description="Security category (e.g., IAM, Storage, Container)")
    resource: str = Field(..., description="The affected resource ARN, ID, or Image Name")
    severity: Severity = Field(..., description="Deterministic severity level")
    confidence: float = Field(1.0, ge=0.0, le=1.0, description="Confidence score of the finding")
    evidence: str = Field(..., description="Raw output or configuration snippet proving the finding")
    impact: str = Field(..., description="Potential security impact if exploited")
    recommendation: str = Field(..., description="Actionable remediation steps")
    source_tool: str = Field(..., description="Tool that generated the finding (e.g., AWS API, Trivy)")
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    
    # Optional field for AI's augmented analysis
    ai_analysis: Optional[str] = Field(None, description="AI-generated context or custom remediation")

class AssessmentSummary(BaseModel):
    """Summary of a completed security assessment."""
    assessment_id: str
    target_environment: str
    start_time: str
    end_time: str
    total_findings: int = 0
    critical_count: int = 0
    high_count: int = 0
    medium_count: int = 0
    low_count: int = 0
    info_count: int = 0
    findings: List[Finding] = []
    tools_used: List[str] = []