from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Number Info API Working 🔥"

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "success": True,
        "result": [
            {
                "id": 1205627021,
                "mobile": "7676184626",
                "name": "Shivalingappa ",
                "father_name": "Durugappa ",
                "address": "S/O: Durugappa!257!!harijana colony!nadanga  !Nadanga!Bellary!Karnataka!583114",
                "alt_mobile": "",
                "circle": "AIRTEL KARNATKA",
                "id_number": "",
                "email": ""
            },
            {
                "id": 1205627022,
                "mobile": "7676184626",
                "name": "Shivalingappa",
                "father_name": "Durugappa",
                "address": "S/O  Durugappa!!257 harijana colony!nadanga!Nadanga Bellary!Karnataka!583114",
                "alt_mobile": "919901542381",
                "circle": "KARNATAKA JIO ",
                "id_number": "",
                "email": ""
            }
        ],
        "credit": "@CodeVortexHere"
    })


# for vercel serverless
def handler(event, context):
    return app(event, context)
