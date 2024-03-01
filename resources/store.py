import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

# blue print divides data into multiple segments
blp = Blueprint("stores", __name__, description="Stores APIs")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try: 
            return stores[store_id]
        except:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
    
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if(store["name"] == store_data["name"]):
                abort(400, message="Store with given name already exists.")
        new_store_id = uuid.uuid4().hex
        new_store = {**store_data, "id": new_store_id}
        stores[new_store_id] = new_store
        return new_store, 201
