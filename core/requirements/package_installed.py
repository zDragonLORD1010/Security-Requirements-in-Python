import shutil
from core.requirement import Requirement


class PackageInstalledRequirement(Requirement):
    EXECUTABLE = ""
    PACKAGE_NAME = ""

    def verify(self):
        return shutil.which(self.EXECUTABLE) is not None

    def remediate(self):
        self.remediation_message = (
            f"Install package " f"{self.PACKAGE_NAME} " f"manually."
        )
        return False
