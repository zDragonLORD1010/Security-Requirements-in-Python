from core.registry import register
from core.requirements.package_installed import PackageInstalledRequirement


@register
class UBTU22232150(PackageInstalledRequirement):
    id = "UBTU-22-232150"
    title = "rsyslog package must be installed"
    severity = "MEDIUM"
    PACKAGE_NAME = "rsyslog"
    EXECUTABLE = "rsyslogd"
