import os
import django
import logging
from flask import Blueprint, request
from flask_restx import Resource

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'mysite.settings'
)
django.setup()

from financial_goal.models import *
from financial_goal.schema.finance_media import FinanceMediaGetSchema


news_blueprint = Blueprint('news_blueprint', __name__)

logger = logging.getLogger(__name__)

class NewsAPI(Resource):

    def get(self) -> dict:
        finance_data = FinanceMedia.objects.all().order_by('-created_on')
        results = []
        for finance in finance_data:
            data = {
                "name": finance.name,
                "media_type": finance.media_type,
                "description": finance.description,
                "link": finance.link,
                "tag": finance.tag,
            }
            results.append(data)
        return results


class DetailsAPI(Resource):

    def get(self) -> dict:
        article_data = UserArticles.objects.all().order_by('-created_on')
        income_range_data = IncomeRange.objects.all().order_by('-created_on')
        occupation_data = Occupation.objects.all().order_by('-created_on')
        financegoal_data = FinanceGoal.objects.all().order_by('-created_on')
        results = []
        results.append({'article_data':[article.name for article in article_data]})
        results.append(
            {'income_data':[
                {"above":income.above, "below": income.below} for income in income_range_data]}
            )
        results.append({'occupation_data':[occupation.name for occupation in occupation_data]})
        results.append({'financegoal_data':[financegoal.name for financegoal in financegoal_data]})
        return results
        