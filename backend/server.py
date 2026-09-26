from flask import Flask, jsonify
from flask_cors import CORS

from app import check_plant


app = Flask(__name__)
CORS(app)


@app.route("/api/plant", methods=["GET"])
def get_plant():
    plant_data = check_plant()
    return jsonify(plant_data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)