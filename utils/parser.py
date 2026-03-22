import re

def parse_text_to_json(text):
    """
    Converts unstructured LLM output into structured resume/job JSON.
    Works as fallback when JSON parsing fails.
    """

    data = {
        "name": "",
        "contact": {
            "email": "",
            "phone": ""
        },
        "summary": "",
        "skills": [],
        "experience": [],
        "projects": [],
        "education": "",
        "achievements": []
    }

    if not text:
        return data

    lines = text.split("\n")
    current_section = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # 🔥 Remove markdown
        line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)

        lower = line.lower()

        # 🔹 Detect sections
        if "summary" in lower:
            current_section = "summary"
            continue

        elif "skills" in lower:
            current_section = "skills"
            continue

        elif "experience" in lower:
            current_section = "experience"
            continue

        elif "project" in lower:
            current_section = "projects"
            continue

        elif "education" in lower:
            current_section = "education"
            continue

        elif "achievement" in lower:
            current_section = "achievements"
            continue

        # 🔹 Extract name (first non-section line)
        if not data["name"]:
            data["name"] = line
            continue

        # 🔹 Extract email
        if "@" in line and "." in line:
            data["contact"]["email"] = line

        # 🔹 Extract phone (simple)
        if re.search(r"\d{10}", line):
            data["contact"]["phone"] = line

        # 🔹 Fill sections
        if current_section == "summary":
            data["summary"] += line + " "

        elif current_section == "skills":
            if line.startswith("-"):
                data["skills"].append(line[1:].strip())
            else:
                data["skills"].append(line)

        elif current_section == "experience":
            data["experience"].append(line)

        elif current_section == "projects":

            # 🔹 Description line
            if line.startswith("-"):
                if data["projects"]:
                    data["projects"][-1] += ": " + line[1:].strip()

            else:
                # 🔹 Treat as new project ONLY if it's not too long
                # (to avoid merging random text)
                if len(line.split()) <= 8:
                    data["projects"].append(line)

        elif current_section == "education":
            data["education"] += line + " "

        elif current_section == "achievements":
            data["achievements"].append(line)

    # 🔥 Final cleanup

    data["summary"] = data["summary"].strip()
    data["education"] = data["education"].strip()

    # Remove duplicates
    data["skills"] = list(set(data["skills"]))
    data["projects"] = list(set(data["projects"]))

    return data
