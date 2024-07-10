import uuid
from flask import  jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from db import stores

blp = Blueprint("Stores", __name__, description="Operations on stores")

@blp.route("/store")
class Store(MethodView):
    def get(self):
        return jsonify({"stores": list(stores.values())})

    def post(self):
        store_data = request.get_json()
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201
    
    def delete(self):
        item_data = request.get_json()
        try:
            del stores[item_data["uuid"]]
        except KeyError:
            return {"message":"Store not found"}, 404
        return {"message":"Store deleted"}, 200

