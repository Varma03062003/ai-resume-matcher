import streamlit as st
from utils import (
    extract_resume_text,
    clean_text,
    calculate_similarity,
    extract_skills
)

# Page config
st.set_page_config(page_title="AI Resume Matcher", layout="centered")
st.title("📄 AI Resume Matcher")

# Sidebar
st.sidebar.header("ℹ️ About")
st.sidebar.write(
    "This AI Resume Matcher compares a resume with a job description "
    "using NLP techniques like TF-IDF and cosine similarity."
)
st.sidebar.write("Built with Python & Streamlit")
    
# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
jd_text = st.text_area("Paste Job Description", height=200)

# Show extracted resume text
if resume_file:
    resume_text = extract_resume_text(resume_file)
    st.subheader("Extracted Resume Text (Preview)")
    st.info("Showing first 800 characters of extracted resume text")
    st.write(resume_text[:800])

# Main logic (only when both inputs exist)
if resume_file and jd_text:
    # Clean texts
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    st.success("Resume and Job Description processed successfully ✅")

    # Analyze button
    if st.button("Analyze Match"):
        # ---- MATCH SCORE ----
        score = calculate_similarity(resume_clean, jd_clean)

        st.subheader("📊 Resume Match Score")

        if score >= 70:
            st.success(f"Strong match: {score}%")
        elif score >= 40:
            st.warning(f"Moderate match: {score}%")
        else:
            st.error(f"Low match: {score}%")

        st.progress(score / 100)

        # ---- SKILL EXTRACTION ----
        resume_skills = extract_skills(resume_clean)
        jd_skills = extract_skills(jd_clean)

        missing_skills = list(set(jd_skills) - set(resume_skills))

        st.subheader("🧠 Skills Found in Resume")
        st.write(resume_skills)

        st.subheader("❌ Missing Skills")
        st.write(missing_skills)

        # ---- SUGGESTIONS ----
        st.subheader("💡 Suggestions")
        if missing_skills:
            for skill in missing_skills:
                st.write(f"• Add projects or experience related to **{skill}**")
        else:
            st.write("Your resume already matches the job requirements well!")
