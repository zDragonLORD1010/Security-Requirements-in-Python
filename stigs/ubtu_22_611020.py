from core.registry import register
from core.requirements.file_owner import FileOwnerRequirement


@register
class UBTU22611020(FileOwnerRequirement):
    id = "UBTU-22-611020"
    title = "/etc/shadow owner must be root"
    severity = "HIGH"
    FILE = "/etc/shadow"
    EXPECTED_OWNER = "root"
