from core.registry import register
from core.requirements.file_group import FileGroupRequirement


@register
class UBTU22232135(FileGroupRequirement):
    id = "UBTU-22-232135"
    title = "/var/log/syslog group owner must be adm"
    severity = "MEDIUM"
    FILE = "/var/log/syslog"
    EXPECTED_GROUP = "adm"
