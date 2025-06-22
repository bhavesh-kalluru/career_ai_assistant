import streamlit as st
from modules import resume_parser, skill_gap, resource_recommender, job_scraper
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("💼 Career AI Assistant")

# Resume Upload
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
if uploaded_file:
    resume_path = f"temp_resume.pdf"
    with open(resume_path, "wb") as f:
        f.write(uploaded_file.read())

    resume_text = resume_parser.extract_text_from_pdf(resume_path)

    # Goal
    goal = st.text_input("🎯 Enter your dream job title (e.g., Data Scientist)")

    # Job Type
    job_type = st.selectbox("📋 Choose Job Type", ["all", "freelance", "full-time", "remote", "contract"])

    if st.button("🚀 Analyze & Recommend"):
        # Skill Gap
        with st.spinner("Analyzing skill gap..."):
            gap = skill_gap.analyze_skill_gap(resume_text, goal)
        st.success("✅ Skill Gap Report")
        st.text_area("Skill Gap Details", gap, height=250)

        # Learning Resources
        st.subheader("📚 Learning Resources")
        links = resource_recommender.recommend_courses(goal)
        for link in links:
            st.markdown(f"- [Watch Here]({link})")

        # Jobs
        jobs = job_scraper.find_jobs("data scientist", job_type="freelance")
        st.subheader("💼 Jobs Matching Your Goal")
        for job in jobs:
            st.markdown(f"🔹 **{job['title']}**\n\n{job['description']}\n[Apply Here]({job['link']})\n")
