from core.registry import register
from core.requirements.identity_uniqueness import IdentityUniquenessRequirement


@register
class UBTU22411015(IdentityUniquenessRequirement):
    id = "UBTU-22-411015"
    title = "Duplicate UIDs must not exist"
    severity = "MEDIUM"
    FILE = "/etc/passwd"
    COLUMN = 2
    DESCRIPTION = "UIDs"
