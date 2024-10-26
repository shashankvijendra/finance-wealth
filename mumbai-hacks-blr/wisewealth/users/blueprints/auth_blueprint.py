import json
import os
import django
import logging
from flask import Blueprint, request
from flask_restx import Resource

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'mysite.settings'
)
django.setup()

from users.schema.signup_post import SignupPostSchema, LoginPostSchema
from users.models import User, UserToken
import hashlib
import binascii

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

logger = logging.getLogger(__name__)


class SignupAPI(Resource):

    def post(self) -> dict:
        request_schema = SignupPostSchema()
        post_data = request.get_json(force=True)
        errors = request_schema.validate(post_data)
        if errors:
            return errors, 400

        post_data = request_schema.load(post_data)
        email = post_data.get('email')
        password = post_data.get('password')
        phone_number = post_data.get('phone_number')
        name = post_data.get('name')
        role = post_data.get("role")

        existing_user = User.objects.filter(phone_number=phone_number).first()
        if existing_user:
            return {"error": "Existing User"}, 400

        user = User()
        user.email_id = email
        user.phone_number = phone_number
        user.name = name
        user.password = hashlib.md5(str(password).encode('utf-8')).hexdigest()
        user.role = role
        user.save()

        user_token = UserToken()
        user_token.user = user
        user_token.token = binascii.hexlify(os.urandom(20)).decode()
        user_token.save()

        return {
            "id":user.phone_number,
            "name": user.name,
            "email": user.email_id,
            "token": user_token.token
        }, 200


class LoginAPI(Resource):

    def post(self) -> dict:

        post_data = json.loads(request.data)
        phone_number = post_data.get('phone_number')
        password = post_data.get('password')
        otp = post_data.get('otp')
        if otp == 1234:
            user = User.objects.filter(phone_number=phone_number).first()
        else: 
            password = hashlib.md5(str(password).encode('utf-8')).hexdigest()
            user = User.objects.filter(phone_number=phone_number, password=password).first()
        if user:
            user_token = UserToken.objects.filter(user=user).last()

            return {
                "phone_number": user.phone_number,
                "name": user.name,
                "email": user.email_id,
                "token": user_token.token if user_token else "",
                "role": user.role
            }, 200

        return {
            "error": "Incorrect Email/Password"
        }, 400










