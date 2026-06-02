from core.registry import register
from core.requirements.identity_uniqueness import IdentityUniquenessRequirement


@register
class UBTU22411020(IdentityUniquenessRequirement):
    id = "UBTU-22-411020"
    title = "Duplicate usernames must not exist"
    severity = "MEDIUM"
    FILE = "/etc/passwd"
    COLUMN = 0
    DESCRIPTION = "usernames"
