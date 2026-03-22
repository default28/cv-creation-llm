## using gemma:2b
# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"

# def query_gemma(prompt):
#     try:
#         response = requests.post(
#             OLLAMA_URL,
#             json={
#                 "model": "gemma:2b",
#                 "prompt": prompt,
#                 "stream": False
#             }
#         )

#         print("\n🔍 DEBUG INFO:")
#         print("Status Code:", response.status_code)
#         print("Response:", response.text)

#         response.raise_for_status()

#         return response.json()["response"]

#     except requests.exceptions.ConnectionError:
#         print("❌ Cannot connect to Ollama. Is it running?")
#         raise

#     except Exception as e:
#         print("❌ Full Error:", str(e))
#         raise

# using lamma3
import requests

def query_gemma(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",   # ✅ updated
        "prompt": prompt,
        "stream": False,
        "options": {
             "temperature": 0.3   # 🔥 lower = more structured
         }
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Ollama error: {response.text}")

    return response.json()["response"]
