# llm/prompts.py

def extraction_prompt(resume_text):
    return f"""
You are an AI that extracts structured resume data.

Return ONLY valid JSON.

STRICT RULES:
- DO NOT return text
- DO NOT explain anything
- DO NOT use markdown
- Ensure ALL fields are present

FORMAT:

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
