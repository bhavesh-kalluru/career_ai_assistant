import os
os.environ["OPENAI_API_KEY"] = "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"

from openai import OpenAI

def analyze_skill_gap(resume_text, target_role):
    client = OpenAI()  # no api_key param, picks from env var

    prompt = f"""Resume:\n{resume_text}\n
Career Goal: {target_role}\n
Analyze the candidate's skills. List current skills, missing skills, and suggest steps to fill the gap.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

