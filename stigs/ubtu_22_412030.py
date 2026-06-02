from core.registry import register
from core.requirements.tmout import TMOUTRequirement


@register
class UBTU22412030(TMOUTRequirement):
    id = "UBTU-22-412030"
    title = "Session timeout must be 900 seconds"
    severity = "MEDIUM"
    EXPECTED_VALUE = 900
