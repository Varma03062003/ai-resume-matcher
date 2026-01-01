# AI Resume Matcher

An AI-powered web application that compares a candidate’s resume with a job description
and provides a match score, missing skills, and improvement suggestions.

## Features
- PDF resume upload
- Job description analysis
- Resume–JD match score using TF-IDF & cosine similarity
- Skill extraction and gap analysis
- Actionable resume improvement suggestions
- Interactive web UI with Streamlit

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- NLTK
- PyPDF2

## How It Works
1. Resume PDF text is extracted and cleaned
2. Job description text is preprocessed
3. TF-IDF vectorization converts text to numerical form
4. Cosine similarity computes the match percentage
5. Skills are extracted and compared to find gaps

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
