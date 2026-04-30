import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_website(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You generate complete websites using HTML, CSS, and JavaScript in a single file."},
            {"role": "user", "content": f"Create a full responsive website for: {prompt}"}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
