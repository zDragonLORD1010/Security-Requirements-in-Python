from pathlib import Path
from core.requirement import Requirement


class RequiredFileRequirement(Requirement):
    FILE = ""
    DEFAULT_CONTENT = ""
    DESCRIPTION = ""

    def verify(self):
        return Path(self.FILE).exists()

    def remediate(self):
        try:
            Path(self.FILE).write_text(self.DEFAULT_CONTENT)
            return True
        except Exception:
            return False
