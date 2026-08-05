from flask import Flask, request, jsonify
from flask_cors import CORS

from fog_controller import traffic_decision
from ids import detect_intrusion
from attack_simulator import simulate_attack
from security import authenticate, encrypt_data

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    # 🔐 Authentication
    token = request.headers.get("Authorization")
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401

    # 📥 Input from UI
    data = request.json
    vehicles = int(data["vehicle_count"])
    speed = int(data["avg_speed"])

    # 🧠 Fog decision logic
    decision = traffic_decision(vehicles)

    # 🛡 Security checks
    intrusion = detect_intrusion(vehicles, speed)
    attack = simulate_attack()

    # 🚦 Traffic light mapping (NOW SUPPORTS YELLOW)
    if decision == "RED":
        light = "red"
    elif decision == "YELLOW":
        light = "yellow"
    else:
        # GREEN NORMAL or GREEN EXTENDED
        light = "green"

    # 📤 Response to frontend
    return jsonify({
        "vehicles": vehicles,
        "speed": speed,
        "decision": decision,
        "light": light,
        "intrusion": intrusion,
        "attack": attack,
        "security": encrypt_data("SECURE")
    })

if __name__ == "__main__":
    app.run(debug=True)