import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

VOICE_ID = "hpp4J3VqNfWAUOO0d1Us"


def generate_voice(message):
    audio = client.text_to_speech.convert(
        text=message,
        voice_id=VOICE_ID,
        model_id="eleven_multilingual_v2"
    )

    return b"".join(audio)