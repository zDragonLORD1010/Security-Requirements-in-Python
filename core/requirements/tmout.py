from pathlib import Path
from core.requirement import Requirement


class TMOUTRequirement(Requirement):
    FILE = "/etc/profile.d/99-terminal_tmout.sh"
    EXPECTED_VALUE = 900

    def verify(self):
        p = Path(self.FILE)
        if not p.exists():
            return False
        return f"TMOUT=" f"{self.EXPECTED_VALUE}" in p.read_text()

    def remediate(self):
        try:
            Path(self.FILE).write_text(f"TMOUT=" f"{self.EXPECTED_VALUE}" "\\n")
            return True
        except Exception:
            return False
