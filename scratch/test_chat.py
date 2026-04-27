import requests

url = "http://127.0.0.1:5000/api/chat"
payload = {"query": "How many students are there?"}

print("Testing AI Chat API...")
try:
    response = requests.post(url, json=payload, timeout=130)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
