from core.registry import register
from core.requirements.required_file import RequiredFileRequirement


@register
class UBTU22232155(RequiredFileRequirement):
    id = "UBTU-22-232155"
    title = "rsyslog configuration must exist"
    severity = "MEDIUM"
    FILE = "/etc/rsyslog.conf"
    DEFAULT_CONTENT = "# rsyslog configuration\n"
