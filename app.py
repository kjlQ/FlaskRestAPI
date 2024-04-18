from flask import Flask, request, jsonify

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.route("/store", methods=["GET"])
def get_stores():
    return jsonify({"stores": stores})

@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(stores), 201

@app.route("/store/add/item", methods=["POST"])
def add_item():
    request_data = request.get_json()
    for store in stores:
        if store["name"] == request_data["store_name"]:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return jsonify(stores), 201
    return {"message":"Not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
