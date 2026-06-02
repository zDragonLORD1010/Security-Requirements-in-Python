from core.registry import register
from core.requirements.required_file import RequiredFileRequirement


@register
class UBTU22412000(RequiredFileRequirement):
    id = "UBTU-22-412000"
    title = "Message of the Day must exist"
    severity = "LOW"
    FILE = "/etc/motd"
    DEFAULT_CONTENT = "Authorized access only\n"
