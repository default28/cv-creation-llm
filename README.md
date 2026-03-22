
# 📄 CV Creation using LLMs

## 🚀 Overview

This project demonstrates how **Large Language Models (LLMs)** can automate resume creation, tailoring, and optimization based on job descriptions.

It is designed as a **capstone project** to showcase:

* Resume parsing
* Job description analysis
* Resume tailoring
* ATS optimization
* Iterative refinement

---

## 🎯 Features

### ✅ Resume Data Extraction

* Supports **PDF, DOCX, TXT**
* Extracts:

  * Name, Contact
  * Skills, Experience
  * Education, Projects

---

### ✅ Job Description Parsing

* Accepts:

  * File upload (PDF/DOCX)
  * Manual input
* Extracts:

  * Requirements
  * Responsibilities
  * Keywords

---

### ✅ Resume Tailoring (Core Feature)

* Aligns resume with job requirements
* Injects relevant keywords
* Rewrites content professionally
* Generates ATS-friendly CV

---

### ✅ ATS Feedback System

* Match score (0–100%)
* Missing keywords
* Improvement suggestions

---

### ✅ Iterative Refinement

* Edit resume in UI
* Re-run LLM for improvements
* Continuous optimization loop

---

### ✅ Output Generation

* Generates structured **DOCX resume**
* Clean formatting (headings, bullets)

---

## 🧠 Tech Stack

* **Python**
* **Ollama (Local LLM runtime)**
* **Gemma (Open-source LLM)**
* **Streamlit (UI)**
* **pdfplumber, python-docx**

---

## 🏗️ Architecture

```
Resume + Job Description
        ↓
Text Extraction
        ↓
LLM Processing
        ↓
Structured JSON
        ↓
Resume Tailoring
        ↓
ATS Feedback
        ↓
Final Resume (DOCX)
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Start Ollama

```bash
ollama run gemma:2b
```

---

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🧪 Sample Inputs

Use files from:

```
sample_data/
```

---

## 📊 Example Output

```json
{
  "match_score": "82%",
  "missing_keywords": ["Docker"],
  "improvement_suggestions": ["Add deployment experience"]
}
```

---

## ⚠️ Challenges & Solutions

| Challenge                 | Solution               |
| ------------------------- | ---------------------- |
| LLM output not structured | JSON + fallback parser |
| Markdown issues           | Cleaning layer         |
| Inconsistent output       | Structured pipeline    |
| ATS parsing issues        | Defensive coding       |

---

## 🚀 Future Enhancements

* Resume templates (modern UI)
* ATS score visualization
* Deployment (web app)
* LinkedIn profile integration

---

## 🎓 Project Context

This project was developed as part of an **AI Capstone Course**, demonstrating real-world applications of LLMs.

---

## 📑 Project Report

[Download Report](report/CV_LLM_Project_Report.pdf)

---

## 👨‍💻 Author

Mini Agrawal

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
