from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(status="ok", time=datetime.now().isoformat())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)