from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# API for patient vitals
@app.route("/vitals")
def vitals():
    data = {
        "heart_rate": random.randint(60, 120),
        "spo2": random.randint(90, 100),
        "bp": f"{random.randint(110,140)}/{random.randint(70,90)}",
        "status": "Normal" if random.randint(0,1) == 0 else "Alert"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
