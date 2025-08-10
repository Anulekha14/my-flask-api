from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (like a mini database)
users = [
    {"id": 1, "name": "Anulekha", "age": 26},
    {"id": 2, "name": "Sudip", "age": 39}
]

# GET → Fetch all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET → Fetch single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

# GET → Fetch single user by Name
@app.route("/users/<string:user_name>", methods=["GET"])
def get_user_by_name(user_name):
    user = next((u for u in users if u["name"] == user_name), None)
    return jsonify(user) if user else ("User not found", 404)


# POST → Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT → Update an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(data)
        return jsonify(user)
    return ("User not found", 404)

# DELETE → Remove a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return ("", 204)

if __name__ == "__main__":
    app.run(debug=True)