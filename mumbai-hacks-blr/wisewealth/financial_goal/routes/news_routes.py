from financial_goal.namespaces.news_namespace import news_namespace
from financial_goal.blueprints.news_blueprint import NewsAPI, DetailsAPI

def initialize_news_routes():
    news_namespace.add_resource(NewsAPI,  '/financial-programs')
    news_namespace.add_resource(DetailsAPI,  '/details')

