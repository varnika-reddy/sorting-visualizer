# ResumeMatch — ATS Resume Analyzer

A web-based tool that analyzes how well your resume matches a job description using **TF-IDF vectorization** and **cosine similarity**. Built with Flask, scikit-learn, and PyMuPDF.

---

## Features

- **Match Score** — Computes a percentage similarity score between your resume and the job description
- **Section Detection** — Automatically detects whether key sections (Skills, Experience, Education, Projects, Certifications) are present in your resume
- **Missing Keywords** — Identifies important keywords from the job description absent in your resume
- **Resume Strength Rating** — Rates overall resume completeness (Complete / Needs Improvement / Incomplete)
- **PDF Upload Support** — Upload a resume PDF directly; text is extracted automatically using PyMuPDF
- **Actionable Tips** — Provides specific suggestions to improve ATS pass rate

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| NLP / Scoring | scikit-learn (TF-IDF, Cosine Similarity) |
| PDF Parsing | PyMuPDF (fitz) |
| Frontend | HTML, CSS (vanilla) |

---

## How It Works

1. **TF-IDF (Term Frequency–Inverse Document Frequency)** converts resume and job description text into numerical vectors, weighting words by how important they are relative to both documents.
2. **Cosine Similarity** measures the angle between the two vectors. A score closer to 1 (100%) means the resume closely matches the job description in terms of language and keywords.
3. **Section Detection** uses keyword pattern matching to identify the presence of standard resume sections.
4. **Keyword Extraction** computes the set difference between job description words and resume words (after filtering stopwords) to surface missing terms.

---

## Setup & Run

```bash
# 1. Clone the repository
git clone https://github.com/varnika-reddy/resume-analyzer.git
cd resume-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## Project Structure

```
resume-analyzer/
├── app.py                  # Flask backend — all logic lives here
├── requirements.txt        # Python dependencies
└── templates/
    ├── index.html          # Input form (paste text or upload PDF)
    └── result.html         # Results page with score, keywords, sections
```

---

## Why TF-IDF + Cosine Similarity?

Most ATS (Applicant Tracking Systems) rank resumes by keyword and phrase relevance against a job description. TF-IDF captures exactly this — it weights words that are distinctive and important rather than common filler words. Cosine similarity then gives a single normalized score regardless of document length, making it a fair comparison metric. This is the same fundamental approach used in real document retrieval and search systems.

---

## Screenshots

> Add screenshots of the home page and result page here after running locally.

---

## Future Improvements

- Named Entity Recognition (NER) for smarter skill extraction
- Support for DOCX resume uploads
- Role-specific keyword databases (e.g. SDE, Data Analyst, Marketing)
- Export results as PDF report
