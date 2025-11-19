from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 Number Info API Working Successfully! 🔥"

@app.route("/info", methods=["GET"])
def info():
    # GET ?num=12345 parameter (optional future use)
    number = request.args.get("num", "")

    # Static JSON Output (YOUR EXACT DATA)
    data = {
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
        "credit": "@BRONX"
    }

    return jsonify(data)

# Required for Vercel Python Runtime
def handler(event, context):
    return app(event, context)
