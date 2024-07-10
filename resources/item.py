import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import items, stores

blp =  Blueprint("Items", __name__, description="Operations on stores")

@blp.route("/item")
class Item(MethodView):
    def post(self):
        item_data = request.get_json()
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201

    def delete():
        item_data = request.get_json()
        try:
            del items[item_data["uuid"]]
        except KeyError:
            return {"message":"Item not found"}, 404
        return {"message":"Item deleted"}, 200


    def put(self,item_id):
        item_data = request.get_json()
        try:
            items[item_id].update(item_data)
        except KeyError:
            return {"message":"Item not found"}, 404
        return {"message":"Item Updated"}, 200

    def get_all(self):
        return {"items": list(items.values())}

    def get(self):
        item_data = request.get_json()
        uuid = item_data["uuid"]
        if uuid in items:
            return items[uuid]
        else:
            abort(404, message="Item not found")

@blp.route("/item/<string:uuid>")
class Item(MethodView):
    def get(self,uuid):
        if uuid in items:
            return items[uuid]
        else:
            abort(404, message="Item not found")
