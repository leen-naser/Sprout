import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)


def analyze_plant(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    prompt = """
Analyze this photo of a plant.

Return ONLY valid JSON with exactly these three fields:

{
  "leaf_condition": "...",
  "discoloration": "...",
  "visible_issue": "..."
}

Describe only things that are visually observable in the image.
Do not diagnose diseases with certainty.
If something cannot be determined from the image, say "not visible" or "unclear".

Examples of possible values:
- leaf_condition: "healthy", "wilting", "drooping", "dry", "unclear"
- discoloration: "none visible", "yellowing", "browning", "spots", "unclear"
- visible_issue: "none obvious", "possible dehydration", "possible leaf damage", "unclear"
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            prompt,
            {
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": image_data,
                }
            },
        ],
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text[7:]

    if text.endswith("```"):
        text = text[:-3]

    return json.loads(text.strip())

def analyze_current_plant(photo_path):
    return analyze_plant(photo_path)

if __name__ == "__main__":
    result = analyze_current_plant("test_images/basil.jpg")
    print(json.dumps(result, indent=2))
