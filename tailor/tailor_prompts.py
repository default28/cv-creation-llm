def tailoring_prompt(resume_json, job_json):
    return f"""
You are an expert ATS resume writer.

TASK:
Rewrite and tailor the resume to match the job description.

STRICT RULES:
- DO NOT use markdown (no ##, **, -, etc.)
- Use plain text only
- Use clear section headings like:
  Name:
  Contact:
  Summary:
  Skills:
  Experience:
  Projects:
  Education:

- Use clean bullet points (start with - or • only)
- DO NOT copy text — rewrite professionally
- Use strong action verbs (Developed, Led, Implemented)
- Align experience with job responsibilities
- Include ALL important job keywords
- Add measurable achievements where possible
- Remove irrelevant content
- Make it ATS-friendly
- DO NOT copy or include job description text directly
- Use job description ONLY to guide improvements
- Rewrite candidate experience in their own context
- Do NOT invent fake companies or roles
- Do NOT add unrelated responsibilities
- Use this EXACT format
- If you cannot return JSON, return plain text with clear section headings only.

EXAMPLE OUTPUT:

Name: John Doe

Contact:
john@email.com

Summary:
Experienced backend engineer...

Skills:
- Java
- Spring Boot

Experience:
Software Engineer | ABC | 2 years
- Developed APIs
- Improved performance

Education:
B.Tech in Computer Science

--------------------------------


Resume Data:
{resume_json}

Job Description:
{job_json}
"""
