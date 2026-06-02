from core.result import RequirementResult


class ExecutionEngine:
    def __init__(self, requirements):
        self.requirements = requirements

    def execute_requirement(self, req):
        events = []
        events.append("Verification started")
        try:
            initial = req.verify()
            if initial:
                events.append("Requirement passed verification")
                return RequirementResult(
                    stig_id=req.id,
                    title=req.title,
                    severity=req.severity,
                    status="PASS",
                    initial_check=True,
                    remediation_attempted=False,
                    remediation_success=False,
                    final_result=True,
                    details=events,
                )
            events.append("Verification failed")
            remediation = req.remediate()
            if hasattr(req, "remediation_message"):
                events.append(req.remediation_message)
            events.append(f"Remediation executed: {remediation}")
            final = req.verify()
            events.append(f"Final verification result: {final}")
            return RequirementResult(
                stig_id=req.id,
                title=req.title,
                severity=req.severity,
                status="PASS" if final else "FAIL",
                initial_check=False,
                remediation_attempted=True,
                remediation_success=remediation,
                final_result=final,
                details=events,
            )
        except Exception as e:
            events.append(f"Exception: {str(e)}")
            return RequirementResult(
                stig_id=req.id,
                title=req.title,
                severity=req.severity,
                status="ERROR",
                initial_check=False,
                remediation_attempted=False,
                remediation_success=False,
                final_result=False,
                details=events,
            )

    def run(self):
        results = []
        for req in self.requirements:
            results.append(self.execute_requirement(req))
        return results
