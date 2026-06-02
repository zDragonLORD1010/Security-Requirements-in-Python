from core.registry import register
from core.requirements.required_file import RequiredFileRequirement


@register
class UBTU22232160(RequiredFileRequirement):
    id = "UBTU-22-232160"
    title = "journald configuration must exist"
    severity = "MEDIUM"
    FILE = "/etc/systemd/journald.conf"
    DEFAULT_CONTENT = "# journald configuration\n"
