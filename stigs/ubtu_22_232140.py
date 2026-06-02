from core.registry import register
from core.requirements.file_owner import FileOwnerRequirement


@register
class UBTU22232140(FileOwnerRequirement):
    id = "UBTU-22-232140"
    title = "/var/log/syslog owner must be root"
    severity = "MEDIUM"
    FILE = "/var/log/syslog"
    EXPECTED_OWNER = "root"
