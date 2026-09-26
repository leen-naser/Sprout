import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from playsound import playsound

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)


def speak(message):
    audio = client.text_to_speech.convert(
        text=message,
        voice_id="hpp4J3VqNfWAUOO0d1Us",  # Bella
        model_id="eleven_multilingual_v2"
    )

    audio_file = "sprout_voice.mp3"

    with open(audio_file, "wb") as file:
        for chunk in audio:
            file.write(chunk)

    playsound(audio_file)

    os.remove(audio_file)

