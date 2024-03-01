from marshmallow import Schema, fields

# define the schema 
class ItemSchema(Schema):
    # put id in it, but this id is only needed when sending data as output 
    id = fields.Str(dump_only=True)

    # name, price and store_id should have String, Float and String datatypes, and are all required
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    # while updating a schema, only name and price are used. but they are not required.
    name = fields.Str()
    price = fields.Str()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)