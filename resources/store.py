import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

# blue print divides data into multiple segments
blp = Blueprint("stores", __name__, description="Stores APIs")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
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
    def get(self):
        return {"stores": list(stores.values())}
    
    def post(self):
        store_data = request.get_json()
        if("name" not in store_data):
            abort(400, message="Bad Request. Ensure 'name' is included in the JSON payload.")
        for store in stores.values():
            if(store["name"] == store_data["name"]):
                abort(400, message="Store with given name already exists.")
        new_store_id = uuid.uuid4().hex
        new_store = {**store_data, "id": new_store_id}
        stores[new_store_id] = new_store
        return new_store, 201