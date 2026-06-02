from core.registry import register
from core.requirements.file_owner import FileOwnerRequirement


@register
class UBTU22611010(FileOwnerRequirement):
    id = "UBTU-22-611010"
    title = "/etc/passwd owner must be root"
    severity = "HIGH"
    FILE = "/etc/passwd"
    EXPECTED_OWNER = "root"
