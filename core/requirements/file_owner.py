import os
import pwd
from core.requirement import Requirement


class FileOwnerRequirement(Requirement):
    FILE = ""
    EXPECTED_OWNER = ""

    def verify(self):
        if not os.path.exists(self.FILE):
            return False
        uid = os.stat(self.FILE).st_uid
        return pwd.getpwuid(uid).pw_name == self.EXPECTED_OWNER

    def remediate(self):
        try:
            uid = pwd.getpwnam(self.EXPECTED_OWNER).pw_uid
            os.chown(self.FILE, uid, -1)
            return True
        except Exception:
            return False
