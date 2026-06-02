from core.registry import register
from core.requirements.identity_uniqueness import IdentityUniquenessRequirement


@register
class UBTU22411030(IdentityUniquenessRequirement):
    id = "UBTU-22-411030"
    title = "Duplicate group names must not exist"
    severity = "MEDIUM"
    FILE = "/etc/group"
    COLUMN = 0
    DESCRIPTION = "group names"
