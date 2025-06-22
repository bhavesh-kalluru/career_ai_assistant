# resource_recommender.py
from youtubesearchpython import VideosSearch

def recommend_courses(skill):
    # TEMPORARY fallback list of tutorial URLs
    tutorials = {
        "data scientist": [
            "https://www.youtube.com/watch?v=ua-CiDNNj30",
            "https://www.youtube.com/watch?v=LHBE6Q9XlzI",
            "https://www.youtube.com/watch?v=xxFYro8QuXA"
        ],
        "data engineer": [
            "https://www.youtube.com/watch?v=OgNq7Zd8e4k",
            "https://www.youtube.com/watch?v=hy7Nx7b2B-4",
            "https://www.youtube.com/watch?v=lD8Qh66Y6iA"
        ],
        # Add more skills and URLs as needed
    }
    skill_lower = skill.lower()
    return tutorials.get(skill_lower, ["https://www.youtube.com/user/edurekaIN"])
