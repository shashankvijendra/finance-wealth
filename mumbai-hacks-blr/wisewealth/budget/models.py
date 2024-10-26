from django.db import models
from common.models import TimeStampedModel
from users.models import User

class Budget(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.CharField(max_length=500, null=True)
    expense = models.CharField(max_length=1000, null=True)

class Transactions(TimeStampedModel):
    id = models.IntegerField(primary_key=True, auto_created=True)
    amount = models.IntegerField()
    type = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
