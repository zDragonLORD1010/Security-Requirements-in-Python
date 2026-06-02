from core.registry import register
from core.requirements.required_file import RequiredFileRequirement


@register
class UBTU22412010(RequiredFileRequirement):
    id = "UBTU-22-412010"
    title = "Login banner must exist"
    severity = "MEDIUM"
    FILE = "/etc/issue"
    DEFAULT_CONTENT = "Authorized access only\n"
