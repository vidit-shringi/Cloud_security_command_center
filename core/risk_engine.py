"""
Risk Engine.
Calculates risk scores, aggregates findings, and enforces deterministic
severity logic before AI analysis is applied.
"""
import uuid
from datetime import datetime, timezone
from typing import List
from core.models import Finding, AssessmentSummary, Severity
from core.logger import log

class RiskEngine:
    def __init__(self):
        self.findings: List[Finding] = []

    def add_finding(self, finding: Finding):
        """Adds a finding and logs it securely."""
        self.findings.append(finding)
        log.debug(f"Finding recorded: {finding.finding_id} - [{finding.severity.value}] on {finding.resource}")

    def generate_summary(self, target_environment: str, tools_used: List[str]) -> AssessmentSummary:
        """Aggregates all findings into a final structured summary."""
        log.info("Calculating risk and generating assessment summary...")
        
        summary = AssessmentSummary(
            assessment_id=f"IS-AUDIT-{uuid.uuid4().hex[:8].upper()}",
            target_environment=target_environment,
            start_time=datetime.now(timezone.utc).isoformat(), # Ideally passed from app start
            end_time=datetime.now(timezone.utc).isoformat(),
            tools_used=tools_used,
            findings=self.findings,
            total_findings=len(self.findings),
            critical_count=sum(1 for f in self.findings if f.severity == Severity.CRITICAL),
            high_count=sum(1 for f in self.findings if f.severity == Severity.HIGH),
            medium_count=sum(1 for f in self.findings if f.severity == Severity.MEDIUM),
            low_count=sum(1 for f in self.findings if f.severity == Severity.LOW),
            info_count=sum(1 for f in self.findings if f.severity == Severity.INFO),
        )
        return summary