from core.registry import register
from core.requirements.file_permission import FilePermissionRequirement


@register
class UBTU22232030(FilePermissionRequirement):
    id = "UBTU-22-232030"
    title = "/var/log/syslog permissions must be 640"
    severity = "MEDIUM"
    FILE = "/var/log/syslog"
    EXPECTED_MODE = "640"
