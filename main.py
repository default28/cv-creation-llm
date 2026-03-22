import os
from extractor.pdf_parser import extract_text_from_pdf
from extractor.docx_parser import extract_text_from_docx
from pipeline.resume_pipeline import extract_resume_data
from job_parser.job_pipeline import extract_job_data
from tailor.tailor_pipeline import generate_tailored_resume
from utils.doc_generator import convert_to_pdf
from review.review_pipeline import get_ats_feedback, refine_resume
from utils.doc_generator import create_docx_from_json


def load_file(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path, "r") as f:
            return f.read()
    else:
        raise Exception("Unsupported file format")


def main():
    print("📄 CV + Job Description Parser")

    choice = input(
        "\nChoose option:\n1. Resume Parsing\n2. Job Description Parsing\n3. Resume Tailoring & Generation\n4. Review & Improve Resume\nEnter: "
    )

    if choice == "1":
        file_path = input("Enter resume file path: ").strip()

        if not os.path.exists(file_path):
            print("❌ File not found")
            return

        print("\n🔍 Extracting text...")
        text = load_file(file_path)

        print("\n🤖 Running LLM extraction...")
        structured_data = extract_resume_data(text)

        print("\n✅ Resume Data:\n")
        print(structured_data)

    elif choice == "2":
        print("\nChoose Job Description Input Method:")
        print("1. Paste manually")
        print("2. Provide file path")

        jd_choice = input("Enter: ").strip()

        if jd_choice == "1":
            print("\nPaste Job Description (type END to finish):\n")

            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)

            job_text = "\n".join(lines)

        elif jd_choice == "2":
            file_path = input("Enter job description file path: ").strip()

            if not os.path.exists(file_path):
                print("❌ File not found")
                return

            print("\n📂 Reading job description file...")
            job_text = load_file(file_path)

        else:
            print("❌ Invalid option")
            return

        print("\n🤖 Parsing Job Description...")
        job_data = extract_job_data(job_text)

        print("\n✅ Job Data:\n")
        print(job_data)

    elif choice == "3":
        resume_path = input("Enter resume file path: ").strip()
        job_path = input("Enter job description file path: ").strip()

        if not os.path.exists(resume_path) or not os.path.exists(job_path):
            print("❌ File not found")
            return

        print("\n🔍 Extracting resume...")
        resume_text = load_file(resume_path)
        resume_json = extract_resume_data(resume_text)

        print("\n🔍 Extracting job description...")
        job_text = load_file(job_path)
        job_json = extract_job_data(job_text)

        print("\n🤖 Generating tailored resume...")
        tailored_json = generate_tailored_resume(resume_json, job_json)

        if not tailored_json:
            print("❌ Failed to generate resume")
            return

        print("\n📄 Creating DOCX file...")

        file_path = create_docx_from_json(tailored_json)

        print(f"\n✅ DOCX saved at: {file_path}")

#         pdf_file = convert_to_pdf(file_path)
#
#         if pdf_file:
#             print(f"✅ PDF saved as {pdf_file}")
#
#         print(f"\n✅ Saved as {file_path}")

    elif choice == "4":
        resume_path = input("Enter generated resume file path: ").strip()
        job_path = input("Enter job description file path: ").strip()

        if not os.path.exists(resume_path) or not os.path.exists(job_path):
            print("❌ File not found")
            return

        resume_text = load_file(resume_path)
        job_text = load_file(job_path)
        job_json = extract_job_data(job_text)

        current_resume = resume_text

        while True:
            print("\n📊 ATS Feedback:")
            feedback = get_ats_feedback(current_resume, job_json)

            print("Match Score:", feedback.get("match_score"))
            print("Missing Keywords:", feedback.get("missing_keywords"))
            print("Suggestions:", feedback.get("improvement_suggestions"))

            print("\n✏️ Edit your resume below (type END to finish):\n")

            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)

            edited_resume = "\n".join(lines)

            print("\n🤖 Refining resume...")
            improved_resume = refine_resume(edited_resume, job_json)

            print("\n✅ Improved Resume:\n")
            print(improved_resume)

            current_resume = improved_resume

            cont = input("\nDo you want to refine again? (y/n): ").strip().lower()
            if cont != "y":
                break

    else:
        print("❌ Invalid option")


if __name__ == "__main__":
    main()
