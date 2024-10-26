from ..namespaces.auth_namespace import auth_namespace
from users.namespaces.user_namespace import user_namespace
from ..blueprints.auth_blueprint import SignupAPI, LoginAPI
from users.blueprints.user_blueprint import UserAPI


def initialize_authentication_routes():
    auth_namespace.add_resource(SignupAPI, '/register')
    auth_namespace.add_resource(LoginAPI, '/login')
    user_namespace.add_resource(UserAPI, '/profile')

