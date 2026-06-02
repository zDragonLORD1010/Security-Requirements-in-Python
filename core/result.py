from dataclasses import dataclass


@dataclass
class RequirementResult:
    stig_id: str
    title: str
    severity: str
    status: str
    initial_check: bool
    remediation_attempted: bool
    remediation_success: bool
    final_result: bool
    details: list
