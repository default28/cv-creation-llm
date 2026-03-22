import re

def clean_markdown(text):
    # Remove markdown symbols
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"#+\s*", "", text)

    # Remove backticks
    text = text.replace("```", "")

    return text.strip()
