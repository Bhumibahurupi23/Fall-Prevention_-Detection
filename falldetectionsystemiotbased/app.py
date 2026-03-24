from flask import Flask, render_template, jsonify
import serial
import threading
import time

app = Flask(__name__)

# --- CONFIG ---
SERIAL_PORT = 'COM9'   # Change to your port (e.g., '/dev/ttyUSB0' on Linux/Mac)
BAUD_RATE = 9600

latest_status = {"status": "SAFE", "timestamp": time.time()}
ser = None

def read_serial():
    global latest_status, ser
    while True:
        try:
            if ser is None or not ser.is_open:
                ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
                print(f"Connected to {SERIAL_PORT}")

            line = ser.readline().decode('utf-8').strip()
            if line in ("COLLISION", "SAFE"):
                latest_status = {"status": line, "timestamp": time.time()}
                print(f"[Serial] {line}")

        except serial.SerialException as e:
            print(f"Serial error: {e}")
            ser = None
            time.sleep(2)
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(1)

# Start background serial reader
thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify(latest_status)

if __name__ == '__main__':
    app.run(debug=True)