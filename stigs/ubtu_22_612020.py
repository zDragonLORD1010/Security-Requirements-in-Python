from core.registry import register
from core.requirements.file_permission import FilePermissionRequirement


@register
class UBTU22612020(FilePermissionRequirement):
    id = "UBTU-22-612020"
    title = "/etc/shadow permissions must be 640"
    severity = "HIGH"
    FILE = "/etc/shadow"
    EXPECTED_MODE = "640"
