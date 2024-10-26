import os
import django
import logging
from flask import Blueprint, request
from flask_restx import Resource
from users.schema.user_details_get import UserSchema

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'mysite.settings'
)
django.setup()

from users.models import User


authentication_blueprint = Blueprint('user_blueprint', __name__)

logger = logging.getLogger(__name__)

class UserAPI(Resource):

    def get(self, phone_number) -> dict:
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist as err:
            return {
                "error": "User Not Exists"
            }, 400
        return {
                "id": user.id,
                "name": user.name,
                "email": user.email_id,
                "token": "",
                "role": user.role
            }, 200

        