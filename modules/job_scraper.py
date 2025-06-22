from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing from your environment variables.")

client = OpenAI(api_key=api_key)

def find_jobs(skill, job_type="freelance"):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful job assistant that only returns valid JSON."},
                {"role": "user", "content": f"Give 5 recent {job_type} or remote job listings related to '{skill}'. For each, include title, short description, and apply link. Only return as JSON array."}
            ],
            functions=[
                {
                    "name": "return_jobs",
                    "description": "Returns a list of job opportunities.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "jobs": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "title": {"type": "string"},
                                        "description": {"type": "string"},
                                        "link": {"type": "string"}
                                    },
                                    "required": ["title", "description", "link"]
                                }
                            }
                        },
                        "required": ["jobs"]
                    }
                }
            ],
            function_call={"name": "return_jobs"},
            temperature=0.5,
        )

        jobs = response.choices[0].message.function_call.arguments
        jobs_dict = json.loads(jobs)
        return jobs_dict["jobs"]

    except Exception as e:
        print("❌ GPT Function Calling Error:", e)
        return [{
            "title": "No jobs found",
            "description": "GPT response failed to parse as JSON.",
            "link": ""
        }]
