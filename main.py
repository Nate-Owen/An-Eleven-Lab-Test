import requests

API_KEY = "sk_128c8d2c71ea492be638d4696f2ae9682556ce12f4dee0ff"

url = "https://api.elevenlabs.io/v1/text-to-speech/Support Agent"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}
data = {
    "text": "Hello from ElevenLabs, this is your first GitHub test voice!",
    "model_id": "agent_3501k9401jrpes08z8ah126tdtys"
}

response = requests.post(url, headers=headers, json=data)

with open("output.mp3", "wb") as f:
    f.write(response.content)

print("✅ Done! Check output.mp3 for your generated voice.")
