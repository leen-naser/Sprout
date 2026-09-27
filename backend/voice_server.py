from flask import Flask, request, Response
from flask_cors import CORS
from backend.voice import generate_voice

app = Flask(__name__)
CORS(app)


@app.route("/api/voice", methods=["POST"])
def voice():
    data = request.get_json()
    message = data["message"]

    audio = generate_voice(message)

    return Response(audio, mimetype="audio/mpeg")


if __name__ == "__main__":
    app.run(port=5001)