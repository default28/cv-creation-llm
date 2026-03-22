# review/feedback_prompt.py

def refine_resume_prompt(edited_resume, job_json):
    return f"""
You are an expert resume reviewer.

Task:
Improve the edited resume based on the job description.

Instructions:
- Fix grammar and clarity
- Add missing keywords from job description
- Strengthen bullet points with action verbs
- Add measurable achievements if possible
- Keep it ATS-friendly

Edited Resume:
{edited_resume}

Job Description:
{job_json}

Return improved resume only.
"""


def ats_feedback_prompt(resume_text, job_json):
    return f"""
You are an ATS system.

Analyze resume vs job description.

Return ONLY valid JSON:

{{
  "match_score": "0-100%",
  "matched_keywords": [],
  "missing_keywords": [],
  "improvement_suggestions": []
}}

Rules:
- Extract important keywords from job description
- Compare with resume
- Give realistic score
- Suggest improvements
- DO NOT return text.
- DO NOT explain anything.

Resume:
{resume_text}

Job Description:
{job_json}
"""
