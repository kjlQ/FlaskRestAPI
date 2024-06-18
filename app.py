import uuid
from flask import Flask, jsonify, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)

@app.get("/store")
def get_stores():
    return jsonify({"stores": list(stores.values())})


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201

@app.delete("/item")
def delete_item():
    item_data = request.get_json()
    try:
        del items[item_data["uuid"]]
    except KeyError:
         return {"message":"Item not found"}, 404
    return {"message":"Item deleted"}, 200


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    try:
        items[item_id].update(item_data)
    except KeyError:
         return {"message":"Item not found"}, 404
    return {"message":"Item Updated"}, 200

@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/item")
def get_item():
    item_data = request.get_json()
    uuid = item_data["uuid"]
    if uuid in items:
        return items[uuid]
    else:
        abort(404, message="Item not found")

if __name__ == "__main__":
    app.run(debug=True)
