import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_gemma(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )

        print("\n🔍 DEBUG INFO:")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        return response.json()["response"]

    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama. Is it running?")
        raise

    except Exception as e:
        print("❌ Full Error:", str(e))
        raise
