from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for demonstration purposes
keys_db = {
    "raju123": {"expiry_date": "2024-11-30"},
    "test_key": {"expiry_date": "2024-12-31"},
}

@app.route('/validate_key', methods=['POST'])
def validate_key():
    data = request.json
    access_key = data.get("access_key")

    if access_key in keys_db:
        expiry_date = datetime.strptime(keys_db[access_key]["expiry_date"], "%Y-%m-%d")
        if datetime.now() <= expiry_date:
            return jsonify({"status": "valid", "message": "Access granted"}), 200
        else:
            return jsonify({"status": "expired", "message": "Key expired"}), 403
    else:
        return jsonify({"status": "invalid", "message": "Invalid key"}), 403

if __name__ == '__main__':
    app.run(debug=True)
