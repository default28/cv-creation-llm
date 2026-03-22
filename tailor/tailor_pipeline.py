# tailor/tailor_pipeline.py

import json
from llm.gemma_client import query_gemma
from tailor.tailor_prompts import tailoring_prompt
import re


def generate_tailored_resume(resume_json, job_json):
    prompt = tailoring_prompt(resume_json, job_json)
    response = query_gemma(prompt)

    try:
        return json.loads(response)   # ✅ first try JSON
    except:
        print("⚠️ JSON parsing failed")
        print(response)
        return parse_text_to_json(response)   # ✅ fallback

def parse_text_to_json(text):
    data = {
        "name": "",
        "contact": "",
        "summary": "",
        "skills": [],
        "experience": [],
        "projects": [],
        "education": ""
    }

    lines = text.split("\n")

    current_section = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Remove markdown
        line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)

        if "contact" in line.lower():
            current_section = "contact"
        elif "summary" in line.lower():
            current_section = "summary"
        elif "skills" in line.lower():
            current_section = "skills"
        elif "experience" in line.lower():
            current_section = "experience"
        elif "education" in line.lower():
            current_section = "education"
        elif "achievement" in line.lower():
            current_section = "projects"

        else:
            if not data["name"]:
                data["name"] = line
            elif current_section == "contact":
                data["contact"] += line + " "
            elif current_section == "summary":
                data["summary"] += line + " "
            elif current_section == "skills":
                if line.startswith("-"):
                    data["skills"].append(line[1:].strip())
                else:
                    data["skills"].append(line)
            elif current_section == "experience":
                data["experience"].append(line)
            elif current_section == "education":
                data["education"] += line + " "
            elif current_section == "projects":
                data["projects"].append(line)

    return data
