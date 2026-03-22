# review/review_pipeline.py

import json
from llm.gemma_client import query_gemma
from review.feedback_prompt import refine_resume_prompt, ats_feedback_prompt


def refine_resume(edited_resume, job_json):
    prompt = refine_resume_prompt(edited_resume, job_json)
    return query_gemma(prompt)


def get_ats_feedback(resume_text, job_json):
    response = query_gemma(ats_feedback_prompt(resume_text, job_json))

    try:
        return json.loads(response)   # ✅ correct
    except:
        print("⚠️ JSON parsing failed → fallback")

        return {   # ✅ SAME LEVEL as print
            "match_score": "N/A",
            "missing_keywords": [],
            "improvement_suggestions": [response]
        }
