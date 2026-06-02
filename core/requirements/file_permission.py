import os
from core.requirement import Requirement


class FilePermissionRequirement(Requirement):
    FILE = ""
    EXPECTED_MODE = ""

    def verify(self):
        if not os.path.exists(self.FILE):
            return False
        mode = oct(os.stat(self.FILE).st_mode)[-3:]
        return mode == self.EXPECTED_MODE

    def remediate(self):
        try:
            os.chmod(self.FILE, int(self.EXPECTED_MODE, 8))
            return True
        except Exception:
            return False
