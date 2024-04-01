from db import db

class ItemModel(db.Model):
    # mapping between a row in our table to a python class and objects

    # name of table
    __tablename__ = "items"

    # column in table
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(88), unique = True, nullable = False) # max 88 chars, item name is unique, cannot be null
    price = db.Column(db.Float(precision = 2), unique = False, nullable = False)
    # should match the value of id in the stores table
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique = False, nullable = False) # foreign key
    store = db.relationship("StoreModel", back_populates = "items") # populates the item object with the store object that has the matching store id
    
