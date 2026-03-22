from llm.gemma_client import query_gemma
from job_parser.job_prompts import job_extraction_prompt
import json
from utils.parser import parse_text_to_json

def extract_job_data(job_text):
    prompt = job_extraction_prompt(job_text)
    response = query_gemma(prompt)

    try:
        return json.loads(response)
    except:
        print("⚠️ JSON parsing failed. Raw output:")
        return parse_text_to_json(response)
