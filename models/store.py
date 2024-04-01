from db import db

class StoreModel(db.Model):
    # name of table
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(88), unique = True, nullable = False) # max 88 chars, item name is unique, cannot be null
    items = db.relationship("ItemModel", back_populates = "store", lazy = "dynamic")