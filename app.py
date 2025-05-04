from flask import Flask, jsonify, abort
import random
import json

app = Flask(__name__)

def load_quotes():
    try:
        with open("quotes.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"error loading quotes: {e}")
        return []
    
quotes = load_quotes()

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK"}), 200

@app.route("/quotes", methods=["GET"])
def all_quotes():
    return jsonify(quotes), 200

@app.route("/quote/random", methods=["GET"])
def random_quote():
    if quotes:
        return jsonify(random.choice(quotes)), 200
    return jsonify({"error": "no quotes available"}), 404

@app.route("/quote/<int:quote_id>", methods=["GET"])
def quote_by_id(quote_id):
    if 0 <= quote_id <len(quotes):
        return jsonify(quotes[quote_id]), 200
    return abort(404, description="quote not found")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)