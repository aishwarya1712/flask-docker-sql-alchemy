from marshmallow import Schema, fields

# Item Schema without the Store information
class PlainItemSchema(Schema):
    # put id in it, but this id is only needed when sending data as output 
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class ItemUpdateSchema(Schema):
    # while updating a schema, only name and price are used. but they are not required.
    name = fields.Str()
    price = fields.Str()
    store_id = fields.Int()
    
class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

# define the schema 
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only = True)
    store = fields.Nested(PlainStoreSchema(), dump_only = True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only = True)