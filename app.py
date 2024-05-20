import json
import requests

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
data = {
    "model": "llama2",
    "prompt": "¿Por qué el cielo es azul?",
    "system": "Responde como si fueras Son Goku",
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
