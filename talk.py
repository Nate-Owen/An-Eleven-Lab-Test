from dotenv import load_dotenv
load_dotenv()

import os
import requests

API_KEY = os.getenv("XI_API_KEY")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

def speak(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.ok:
        with open("speech.mp3", "wb") as f:
            f.write(response.content)
        print("Spoken:", text)
    else:
        print("Error:", response.status_code, response.text)

while True:
    text = input("What should I say? (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    speak(text)


