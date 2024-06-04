import uuid
from flask import Flask, jsonify, request
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
        return {"message": "Store not found"}, 404
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201

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
        return {"message": "Item not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
