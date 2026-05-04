import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context: str, query: str):

    prompt = f"""
You are an AI logistics assistant.

Use ONLY the context below.

Context:
{context}

Question:
{query}

Give a clear, short answer.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content