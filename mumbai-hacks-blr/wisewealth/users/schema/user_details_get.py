from marshmallow import fields, Schema, validates, ValidationError


class UserSchema(Schema):
    name = fields.String()
    email_id = fields.Email()
    gender = fields.Boolean()
    