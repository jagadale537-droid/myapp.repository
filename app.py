from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(
        application="devops-demo",
        status="running",
        hostname=socket.gethostname()
    )

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

@app.get("/version")
def version():
    return jsonify(
        version=os.getenv("APP_VERSION", "1.0.0")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
