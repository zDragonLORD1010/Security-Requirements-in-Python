from core.registry import register
from core.requirements.file_group import FileGroupRequirement


@register
class UBTU22232170(FileGroupRequirement):
    id = "UBTU-22-232170"
    title = "/var/log/auth.log group must be adm"
    severity = "MEDIUM"
    FILE = "/var/log/auth.log"
    EXPECTED_GROUP = "adm"
