from flask import Flask, request, jsonify
from model import predict_fall
from alert import send_alert

app = Flask(__name__)

latest_data = {"acc": 0, "status": "Safe"}

@app.route("/sensor", methods=["POST"])
def sensor():
    global latest_data

    data = request.json
    ax = data.get("ax", 0)
    ay = data.get("ay", 0)
    az = data.get("az", 0)

    # Calculate magnitude
    acc = (ax**2 + ay**2 + az**2) ** 0.5

    result = predict_fall(acc)

    if result == 1:
        latest_data = {"acc": acc, "status": "Fall Detected"}
        send_alert()
    else:
        latest_data = {"acc": acc, "status": "Safe"}

    return jsonify({"message": "Received"})

@app.route("/status", methods=["GET"])
def status():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)