from core.registry import register
from core.requirements.account_policy import AccountPolicyRequirement


@register
class UBTU22411035(AccountPolicyRequirement):
    id = "UBTU-22-411035"
    title = "Account inactivity must be 35 days"
    severity = "MEDIUM"
    FILE = "/etc/default/useradd"
    PARAMETER = "INACTIVE"
    EXPECTED_VALUE = "35"
