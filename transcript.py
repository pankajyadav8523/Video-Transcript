import requests

def generate_transcript(audio_file, api_key):
    if not api_key:
        raise ValueError("API Key is missing")
    response = requests.post("https://api.transcript.com", files={"file": open(audio_file, "rb")}, headers={"Authorization": f"Bearer {api_key}"})
    return response.json()