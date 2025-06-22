# app.py

import os
from dotenv import load_dotenv
from modules import resume_parser, skill_gap, resource_recommender, job_scraper

# ✅ Load .env variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# ✅ Step 1: Extract resume text
resume_path = "/Users/bhavi/career_ai_assistant/Data/Untitled.pdf"  # Make sure this is a real PDF
resume_text = resume_parser.extract_text_from_pdf(resume_path)

# ✅ Step 2: Ask user for career goal
goal = input("Enter your dream job title (e.g., Data Scientist): ")

# ✅ Step 3: Skill gap analysis using OpenAI
print("\n🔍 Analyzing Skill Gap...")
gap_report = skill_gap.analyze_skill_gap(resume_text, goal)
print(gap_report)

# ✅ Step 4: Recommend learning resources from YouTube
print("\n📚 Recommended Learning Resources:")
resources = resource_recommender.recommend_courses(goal)
for link in resources:
    print(link)

# ✅ Step 5: Scrape freelance jobs
goal = "AI Engineer"  # or take from input()
jobs = job_scraper.find_jobs(goal)
for job in jobs:
    print(f"- {job['title']}: {job['link']}")

