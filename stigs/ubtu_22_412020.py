from core.registry import register
from core.requirements.account_policy import AccountPolicyRequirement


@register
class UBTU22412020(AccountPolicyRequirement):
    id = "UBTU-22-412020"
    title = "Minimum password age must be 1 day"
    severity = "MEDIUM"
    FILE = "/etc/login.defs"
    PARAMETER = "PASS_MIN_DAYS"
    EXPECTED_VALUE = "1"
