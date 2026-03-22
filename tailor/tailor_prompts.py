def tailoring_prompt(resume_json, job_json):
    return f"""
You are a senior professional resume writer and ATS optimization expert.

TASK:
Rewrite and improve the candidate's resume to make it highly professional, ATS-friendly, and aligned with the job.

FORMAT:
{{
  "name": "",
  "contact": "",
  "summary": "",
  "skills": [],
  "experience": [],
  "projects": [],
  "education": ""
}}

STRICT RULES:
- DO NOT include job description text
- DO NOT copy job description sentences
- DO NOT use markdown (no ##, **, etc.)
- DO NOT repeat sections (no duplicate headings)
- Use clean plain text only

IMPROVEMENT RULES:
- DO NOT leave any field empty
- If data is missing → infer from resume
- ALWAYS generate summary (2-3 lines)
- ALWAYS include at least 1 project
- ALWAYS include education
- DO NOT include job description
- Add a strong professional SUMMARY (2–3 lines)
- Use powerful action verbs (Developed, Designed, Optimized, Led)
- Add measurable impact (%, performance, scale)
- Align experience with job requirements
- Prioritize relevant SKILLS at top
- Remove weak or irrelevant content
- Ensure consistent formatting

Resume Data:
{resume_json}

Job Context (for alignment only, DO NOT copy):
{job_json}

IMPORTANT:
If you include job description or extra sections, the answer is incorrect.
If achievements are missing, infer realistic improvements based on experience.

DO NOT start your answer with phrases like:
"Here is", "Below is", "The following is"

Start directly with the name.
If section is empty, then keep it as it is from the input resume.

Return ONLY clean professional resume.
"""
