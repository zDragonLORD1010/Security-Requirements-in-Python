from core.registry import register
from core.requirements.account_policy import AccountPolicyRequirement


@register
class UBTU22412025(AccountPolicyRequirement):
    id = "UBTU-22-412025"
    title = "Maximum password age must be 60 days"
    severity = "MEDIUM"
    FILE = "/etc/login.defs"
    PARAMETER = "PASS_MAX_DAYS"
    EXPECTED_VALUE = "60"
