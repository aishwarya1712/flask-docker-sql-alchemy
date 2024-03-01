import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items

# blue print divides data into multiple segments
blp = Blueprint("items", __name__, description="Items APIs")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    def put(self, item_id):
        item_data = request.get_json()
        if ("price" not in item_data or "name" not in item_data):
            abort(400, message="Bad Request. Ensure 'price' and 'name' are included in the JSON payload.")
        try:
            item = items[item_id]
            item |= item_data # new operator
            return item
        except KeyError:
            abort(400, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
        item_data = request.get_json()
        if("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
            abort(400, message="Bad Request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.")
        if(item_data["store_id"] not in stores):
            abort(404, message="Store not found")
        for item in items.values():
            # check if item already exists in store
            if(item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
                abort(400, "Item already exists in given store.")
        new_item_id = uuid.uuid4().hex
        new_item = {**item_data, "id": new_item_id}
        items[new_item_id] = new_item
        return new_item, 201