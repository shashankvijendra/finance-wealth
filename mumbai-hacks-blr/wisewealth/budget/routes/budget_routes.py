from budget.namespaces.budget_namespace import budget_namespace
from budget.blueprints.budget_blueprint import BudgetAPI, BudgetTransactionAPI

def initialize_budget_routes():
    budget_namespace.add_resource(BudgetAPI,  '/details/<int:phone_number>')
    budget_namespace.add_resource(BudgetTransactionAPI,  '/transactions/<int:phone_number>')

