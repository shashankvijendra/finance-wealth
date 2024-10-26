from marshmallow import fields, Schema, validates, ValidationError


class FinanceMediaGetSchema(Schema):
    name = fields.String()
    media_type = fields.String()
    description = fields.String()
    link = fields.String()
    tag = fields.String()



