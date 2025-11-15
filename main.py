from dotenv import load_dotenv
load_dotenv()

import os
import requests

API_KEY = os.getenv("XI_API_KEY")
print("Loaded key:", API_KEY)
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
TEXT = "Hello from ElevenLabs! This time the API should really speak."


url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}
data = {
    "text": TEXT,
    "model_id": "eleven_multilingual_v2"
}

print("API_KEY:", API_KEY)



response = requests.post(url, headers=headers, json=data)

if response.ok:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("✅ Voice created successfully, check output.mp3")
else:
    print("❌ Error:", response.status_code, response.text)
