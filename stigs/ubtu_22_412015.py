from core.registry import register
from core.requirements.account_policy import AccountPolicyRequirement


@register
class UBTU22412015(AccountPolicyRequirement):
    id = "UBTU-22-412015"
    title = "Password warning age must be 7 days"
    severity = "MEDIUM"
    FILE = "/etc/login.defs"
    PARAMETER = "PASS_WARN_AGE"
    EXPECTED_VALUE = "7"
