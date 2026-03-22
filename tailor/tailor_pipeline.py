# tailor/tailor_pipeline.py

import json
from llm.gemma_client import query_gemma
from tailor.tailor_prompts import tailoring_prompt
import re
from utils.doc_generator import  remove_job_description
from utils.parser import parse_text_to_json


def generate_tailored_resume(resume_json, job_json):

     # 🔥 SAFETY FIX
    if isinstance(resume_json, str):
        resume_json = parse_text_to_json(resume_json)

    prompt = tailoring_prompt(resume_json, job_json)

    response = query_gemma(prompt)

    # 🔥 CLEAN RESPONSE (string level)
    response = remove_job_description(response)

    # 🔥 PARSE JSON
    try:
        data = json.loads(response)
    except:
        data = parse_text_to_json(response)

    # 🔥 FIX EMPTY / MISSING FIELDS (THIS IS YOUR LINE)
    data = fix_resume_json(data, resume_json)

    return data

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


def fix_resume_json(data, original_resume):

    # 🔥 ensure original_resume is dict
    if isinstance(original_resume, str):
        original_resume = parse_text_to_json(original_resume)

    # 🔥 SUMMARY FIX
    if not data.get("summary") or len(data["summary"].strip()) < 10:
        data["summary"] = (
            "Backend Engineer with experience in Java, Spring Boot, and scalable systems."
        )

    # 🔥 PROJECT FIX
    if not data.get("projects"):
        data["projects"] = original_resume.get("projects", [])

    # 🔥 EDUCATION FIX
    if not data.get("education"):
        data["education"] = original_resume.get("education", "B.Tech in Computer Science")

    # 🔥 SKILLS FIX
    if not data.get("skills"):
        data["skills"] = original_resume.get("skills", [])

    return data
