from django.db import models
from common.models import TimeStampedModel

# Create your models here.

class UserArticles(TimeStampedModel):
    name = models.CharField(max_length=200, null=True)
    

class IncomeRange(TimeStampedModel):
    above = models.IntegerField(null=True)
    below = models.IntegerField(null=True)
    
class Occupation(TimeStampedModel):
    name = models.CharField(max_length=500, null=True)
    
class FinanceGoal(TimeStampedModel):
    name = models.CharField(max_length=500, null=True) 
    

class FinanceMedia(TimeStampedModel):
    name = models.CharField(max_length=500, null=True)
    media_type = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=1000, null=True)
    tag =  models.CharField(max_length=100, null=True)
    