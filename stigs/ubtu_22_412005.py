from core.registry import register
from core.requirements.required_file import RequiredFileRequirement


@register
class UBTU22412005(RequiredFileRequirement):
    id = "UBTU-22-412005"
    title = "Remote login banner must exist"
    severity = "MEDIUM"
    FILE = "/etc/issue.net"
    DEFAULT_CONTENT = "Authorized access only\n"
