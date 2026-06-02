import os
import grp
from core.requirement import Requirement


class FileGroupRequirement(Requirement):
    FILE = ""
    EXPECTED_GROUP = ""

    def verify(self):
        if not os.path.exists(self.FILE):
            return False
        gid = os.stat(self.FILE).st_gid
        return grp.getgrgid(gid).gr_name == self.EXPECTED_GROUP

    def remediate(self):
        try:
            gid = grp.getgrnam(self.EXPECTED_GROUP).gr_gid
            os.chown(self.FILE, -1, gid)
            return True
        except Exception:
            return False
