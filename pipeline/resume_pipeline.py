# pipeline/resume_pipeline.py

from llm.gemma_client import query_gemma
from llm.prompts import extraction_prompt
import json

def extract_resume_data(text):
    prompt = extraction_prompt(text)
    response = query_gemma(prompt)

    try:
        return json.loads(response)
    except:
        print("⚠️ JSON parsing failed. Raw output:")
        print(response)
        return response
