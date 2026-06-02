import json
from pathlib import Path
from datetime import datetime


def save_report(results):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    report = {"timestamp": datetime.now().isoformat(), "results": []}
    for r in results:
        report["results"].append(
            {
                "stig_id": r.stig_id,
                "title": r.title,
                "severity": r.severity,
                "status": r.status,
                "initial_check": r.initial_check,
                "remediation_attempted": r.remediation_attempted,
                "remediation_success": r.remediation_success,
                "final_result": r.final_result,
                "details": r.details,
            }
        )

    filename = reports_dir / datetime.now().strftime("report_%Y_%m_%d_%H_%M_%S.json")
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
    return filename
