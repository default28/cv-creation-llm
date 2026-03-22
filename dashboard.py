import streamlit as st
import os

from extractor.pdf_parser import extract_text_from_pdf
from extractor.docx_parser import extract_text_from_docx
from pipeline.resume_pipeline import extract_resume_data
from job_parser.job_pipeline import extract_job_data
from tailor.tailor_pipeline import generate_tailored_resume
from review.review_pipeline import get_ats_feedback, refine_resume
from utils.doc_generator import create_docx_from_json
from tailor.tailor_pipeline import parse_text_to_json


# -------------------------
# File loader
# -------------------------
def load_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        return extract_text_from_pdf("temp.pdf")

    elif uploaded_file.name.endswith(".docx"):
        with open("temp.docx", "wb") as f:
            f.write(uploaded_file.read())
        return extract_text_from_docx("temp.docx")

    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")


# -------------------------
# UI
# -------------------------
st.title("📄 AI Resume Builder (LLM Project)")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
job_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

if st.button("Generate Tailored Resume"):

    if not resume_file or not job_file:
        st.error("Please upload both files")
    else:
        # Extract text
        resume_text = load_file(resume_file)
        job_text = load_file(job_file)

        # Convert to JSON
        resume_json = extract_resume_data(resume_text)
        job_json = extract_job_data(job_text)

        # Generate resume
        tailored_json = generate_tailored_resume(resume_json, job_json)

        if not tailored_json:
            st.error("Failed to generate resume")
        else:
            st.session_state["resume_json"] = tailored_json
            st.session_state["job_json"] = job_json


# -------------------------
# Show & Edit Resume
# -------------------------
if "resume_json" in st.session_state:

    st.subheader("✏️ Edit Resume")

    resume_text = str(st.session_state["resume_json"])

    edited_text = st.text_area("Edit your resume", resume_text, height=400)

    # -------------------------
    # ATS Feedback
    # -------------------------
    # ATS Feedback
    if st.button("📊 Get ATS Feedback"):

        feedback = get_ats_feedback(edited_text, st.session_state["job_json"])

        if isinstance(feedback, dict):
            st.write("### ATS Feedback")
            st.write("Match Score:", feedback.get("match_score"))
            st.write("Missing Keywords:", feedback.get("missing_keywords"))
            st.write("Suggestions:", feedback.get("improvement_suggestions"))
        else:
            st.write("### ATS Feedback")
            st.write(feedback)

    # -------------------------
    # Refine Resume
    # -------------------------
    if st.button("🤖 Refine Resume"):
        improved = refine_resume(edited_text, st.session_state["job_json"])

        # 🔥 convert to JSON
        if isinstance(improved, str):
            improved = parse_text_to_json(improved)

        st.session_state["resume_json"] = improved

        st.success("Resume improved!")

    # -------------------------
    # Download DOCX
    # -------------------------
    if st.button("📄 Download DOCX"):
        resume_data = st.session_state["resume_json"]

        # 🔥 FIX: handle string case
        if isinstance(resume_data, str):
            from tailor.tailor_pipeline import parse_text_to_json
            resume_data = parse_text_to_json(resume_data)

        file_path = create_docx_from_json(resume_data)

        with open(file_path, "rb") as f:
            st.download_button("Download Resume", f, file_name="resume.docx")
