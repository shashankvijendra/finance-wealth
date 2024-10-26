from django.db import models
from common.models import TimeStampedModel
from financial_goal.models import UserArticles, IncomeRange

class User(TimeStampedModel):
    email_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=500, null=True)
    password = models.CharField(max_length=1000, null=True)
    role = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=20)
    phone_number = models.IntegerField(primary_key=True)


class UserToken(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=30)
    

class UserOnboarding(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    occupation = models.CharField(max_length=1000, null=True)
    monthly_income_above = models.IntegerField(null=True)
    monthly_income_below = models.IntegerField(null=True)
    financial_goal = models.CharField(max_length=1000, null=True)
    saving_goal_amt = models.IntegerField()
    is_current_savings = models.BooleanField(default=False)
    preferred_learning_format = models.ManyToManyField(UserArticles, blank=True)

