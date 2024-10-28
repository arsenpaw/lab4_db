from marshmallow import fields, Schema


class AwardSchema(Schema):
    Title = fields.Str(required=True, validate=lambda s: len(s) > 0)
    Description = fields.Str(required=True, validate=lambda s: len(s) > 0)
