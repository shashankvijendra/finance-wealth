from flask import Flask
from flask_restx import Api
from flask_cors import CORS


from users.blueprints.auth_blueprint import authentication_blueprint
from financial_goal.blueprints.news_blueprint import news_blueprint
from budget.blueprints.budget_blueprint import budget_blueprint


from users.namespaces.auth_namespace import auth_namespace
from financial_goal.namespaces.news_namespace import news_namespace
from budget.namespaces.budget_namespace import budget_namespace


from users.routes.auth_routes import initialize_authentication_routes
from financial_goal.routes.news_routes import initialize_news_routes
from budget.routes.budget_routes import initialize_budget_routes



from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
CORS(app)

csrf = CSRFProtect()
csrf.init_app(app)


app.register_blueprint(authentication_blueprint)
app.register_blueprint(news_blueprint)
app.register_blueprint(budget_blueprint)


api = Api(app)
api.add_namespace(auth_namespace)
api.add_namespace(news_namespace)
api.add_namespace(budget_namespace)


initialize_authentication_routes()
initialize_news_routes()
initialize_budget_routes()




if __name__ == "__main__":
    app.run(debug=False)