from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__)

PHONE_IP = "10.168.100.75:8080"  # change if needed

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/data')
def get_data():
    url = f"http://{PHONE_IP}/get?accX&accY&accZ"
    
    res = requests.get(url).json()

    data = {
        "accX": res["buffer"]["accX"]["buffer"][-1],
        "accY": res["buffer"]["accY"]["buffer"][-1],
        "accZ": res["buffer"]["accZ"]["buffer"][-1],
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)