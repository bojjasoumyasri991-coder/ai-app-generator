import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str):

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # ✅ WORKING MODEL
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ LLM ERROR:", e)
        return ""