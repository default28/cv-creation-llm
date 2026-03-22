# llm/prompts.py

def extraction_prompt(resume_text):
    return f"""
You are an AI that extracts structured resume data.

Return ONLY valid JSON in this format:

{{
  "name": "",
  "contact": {{
    "email": "",
    "phone": ""
  }},
  "education": [],
  "experience": [],
  "skills": [],
  "projects": [],
  "achievements": []
}}

Resume:
{resume_text}
"""
