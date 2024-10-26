import json
import os
import django
import logging
from flask import Blueprint, request
from flask_restx import Resource
from budget.models import Budget, Transactions
from users.models import User

os.environ.setdefault(
    'DJANGO_SETTINGS_MODTransactionsULE', 'mysite.settings'
)
django.setup()


budget_blueprint = Blueprint('budget_blueprint', __name__)

logger = logging.getLogger(__name__)

class BudgetAPI(Resource):

    def get(self, phone_number) -> dict:
        try:
            budget = Budget.objects.get(user=phone_number)
        except Budget.DoesNotExist as err:
            return {
                "error": "Budget Not Exists"
            }, 400
        return {
                "name": budget.user.name,
                "income": budget.income,
                "expense": budget.expense
            }, 200

    def post(self, phone_number) -> dict:
        post_data = json.loads(request.data)
        income = post_data.get('income')
        expense = post_data.get('expense')
        try:
            budget = Budget.objects.get(user=phone_number)
        except Budget.DoesNotExist as err:
            budget = Budget()
        user = User.objects.filter(phone_number=phone_number).last()
        if income:
           budget.income = income
        if expense:
           budget.expense = expense 
        budget.user = user
        budget.save()
        return {
                "name": budget.user.name,
                "income": budget.income,
                "expense": budget.expense
            }, 200        


class BudgetTransactionAPI(Resource):

    def get(self, phone_number) -> dict:
        try:
            budget = Budget.objects.get(user=phone_number)
            transactions = Transactions.objects.filter(user=budget.user)
            results = []
            for transaction in transactions:
                results.append(
                    {
                        "amount": transaction.amount,
                        "type": transaction.type
                    }
                )
            return results
        except Budget.DoesNotExist as err:
            return {
                "error": "Budget Not Exists"
            }, 400

    def post(self, phone_number) -> dict:
        post_data = json.loads(request.data)
        type = post_data.get('type')
        amount = post_data.get('amount')
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist as err:
            return {
                "error": "Budget Not Exists"
            }, 400
        transaction = Transactions()
        if type:
           transaction.type = type
        if amount:
           transaction.amount = amount 
        transaction.user = user
        transaction.save()
        return {
                "type": transaction.type,
                "name": user.name,
                "amount": transaction.amount,
                "id": transaction.id
            }, 200           