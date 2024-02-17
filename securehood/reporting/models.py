from django.db import models
from users.models import CustomUser, Address, CommunityMember


class Type(models.Model):
    title = models.CharField(max_length=255)


class Report(models.Model):
    user = models.ForeignKey(CommunityMember, on_delete=models.RESTRICT) # in order to file a report, you MUST be a verfied community member first
    LOW_RISK = 'L'
    MEDIUM_RISK = 'M'
    HIGH_RISK = 'H'
    EMERGENCY = 'E'
    RISK_CHOICES = [
        (LOW_RISK, "Low Risk"),
        (MEDIUM_RISK, 'Medium Risk'), 
        (HIGH_RISK, 'High Risk'), 
        (EMERGENCY, 'Emergency')
    ]
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    risk = models.CharField(max_length=1, choices=RISK_CHOICES, default=EMERGENCY)
    law_enforcement_involve = models.BooleanField()
    
