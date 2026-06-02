from core.registry import register
from core.requirements.file_permission import FilePermissionRequirement


@register
class UBTU22232035(FilePermissionRequirement):
    id = "UBTU-22-232035"
    title = "/var/log/auth.log permissions must be 640"
    severity = "MEDIUM"
    FILE = "/var/log/auth.log"
    EXPECTED_MODE = "640"
