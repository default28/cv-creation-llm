def job_extraction_prompt(job_text):
    return f"""
You are an AI that extracts structured job data.

Return ONLY valid JSON in this format:

{{
  "role": "",
  "company": "",
  "requirements": [],
  "responsibilities": [],
  "skills": [],
  "keywords": []
}}

Instructions:
- Extract concise bullet points
- Remove duplicates
- Infer missing skills if obvious

Job Description:
{job_text}
"""
