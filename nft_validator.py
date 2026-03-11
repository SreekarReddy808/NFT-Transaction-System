from flask import Flask, request, jsonify
import hashlib
import datetime

app = Flask(__name__)

def generate_nft_hash(name, creator, timestamp):
    data = f"{name}{creator}{timestamp}"
    return hashlib.sha256(data.encode()).hexdigest()

@app.route('/validateNFT', methods=['POST'])
def validate_nft():
    data = request.json
    
    name = data.get("name")
    creator = data.get("creator")
    price = data.get("price")

    if not name or not creator or not price:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    timestamp = str(datetime.datetime.now())
    nft_hash = generate_nft_hash(name, creator, timestamp)

    return jsonify({
        "status": "success",
        "nft_hash": nft_hash,
        "timestamp": timestamp
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
