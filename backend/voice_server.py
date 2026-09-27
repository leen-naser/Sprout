from flask import Flask, request, Response, jsonify
from flask_cors import CORS

from backend.voice import generate_voice
from backend.plant_vision import analyze_current_plant
from webcam_test import capture_plant_photo

app = Flask(__name__)
CORS(app)


@app.route("/api/voice", methods=["POST"])
def voice():
    data = request.get_json()
    message = data["message"]

    audio = generate_voice(message)

    return Response(audio, mimetype="audio/mpeg")


@app.route("/api/vision", methods=["GET"])
def vision():
    photo_path = "test_images/webcam_test.jpg"

    capture_plant_photo(photo_path, camera_index=1)
    vision_data = analyze_current_plant(photo_path)

    return jsonify(vision_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)