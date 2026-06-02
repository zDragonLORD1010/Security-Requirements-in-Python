from core.registry import register
from core.requirements.identity_uniqueness import IdentityUniquenessRequirement


@register
class UBTU22411025(IdentityUniquenessRequirement):
    id = "UBTU-22-411025"
    title = "Duplicate GIDs must not exist"
    severity = "MEDIUM"
    FILE = "/etc/group"
    COLUMN = 2
    DESCRIPTION = "GIDs"
