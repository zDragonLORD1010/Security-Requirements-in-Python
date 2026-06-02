from core.requirement import Requirement


class IdentityUniquenessRequirement(Requirement):
    FILE = ""
    COLUMN = 0
    DESCRIPTION = ""

    def verify(self):
        values = set()
        with open(self.FILE) as f:
            for line in f:
                value = line.strip().split(":")[self.COLUMN]
                if value in values:
                    return False
                values.add(value)
        return True

    def remediate(self):
        self.remediation_message = (
            f"Duplicate "
            f"{self.DESCRIPTION} "
            f"detected. "
            f"Automatic remediation "
            f"not supported."
        )
        return False
