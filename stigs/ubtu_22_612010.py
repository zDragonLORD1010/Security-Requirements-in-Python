from core.registry import register
from core.requirements.file_permission import FilePermissionRequirement


@register
class UBTU22612010(FilePermissionRequirement):
    id = "UBTU-22-612010"
    title = "/etc/passwd permissions must be 644"
    severity = "HIGH"
    FILE = "/etc/passwd"
    EXPECTED_MODE = "644"
