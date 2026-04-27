import requests
from app.config import Config


class OllamaService:
    @staticmethod
    def generate_chat_response(prompt):
        payload = {
            "model": Config.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "top_p": 0.9,
                "num_predict": 300
            }
        }

        # Increased timeout to 120s as local LLMs might be slow initially
        response = requests.post(Config.OLLAMA_URL, json=payload, timeout=120)
        return response
