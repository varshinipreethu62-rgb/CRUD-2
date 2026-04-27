import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
payload = {
    "model": "mistral",
    "prompt": "Hello",
    "stream": False
}

print("Sending request to Ollama...")
try:
    response = requests.post(OLLAMA_URL, json=payload, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json().get('response')}")
except Exception as e:
    print(f"Error: {e}")
