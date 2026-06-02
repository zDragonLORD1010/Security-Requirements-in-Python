from pathlib import Path
from core.requirement import Requirement


class AccountPolicyRequirement(Requirement):
    FILE = ""
    PARAMETER = ""
    EXPECTED_VALUE = ""

    def verify(self):
        content = Path(self.FILE).read_text()
        expected = f"{self.PARAMETER}" f"={self.EXPECTED_VALUE}"
        return (
            expected in content
            or f"{self.PARAMETER} " f"{self.EXPECTED_VALUE}" in content
        )

    def remediate(self):
        try:
            path = Path(self.FILE)
            lines = path.read_text().splitlines()
            updated = []
            found = False
            for line in lines:
                if line.strip().startswith(self.PARAMETER):
                    updated.append(f"{self.PARAMETER} " f"{self.EXPECTED_VALUE}")
                    found = True
                else:
                    updated.append(line)
            if not found:
                updated.append(f"{self.PARAMETER} " f"{self.EXPECTED_VALUE}")
            path.write_text("\n".join(updated) + "\n")
            return True
        except Exception:
            return False
