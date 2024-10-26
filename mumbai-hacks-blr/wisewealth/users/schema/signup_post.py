from marshmallow import fields, Schema, validates, ValidationError


class SignupPostSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    phone_number = fields.Integer(required=True)



class LoginPostSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)



