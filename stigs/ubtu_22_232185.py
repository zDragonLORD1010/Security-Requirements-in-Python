from core.registry import register
from core.requirements.file_group import FileGroupRequirement


@register
class UBTU22232185(FileGroupRequirement):
    id = "UBTU-22-232185"
    title = "/var/log/apt/history.log group must be adm"
    severity = "MEDIUM"
    FILE = "/var/log/apt/history.log"
    EXPECTED_GROUP = "adm"
