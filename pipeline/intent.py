import json
import re
from utils.llm import call_llm

def extract_json(text: str):
    """Extract JSON from messy LLM output"""
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass
    return None


def extract_intent(user_input: str):
    prompt = f"""
You are a strict JSON generator.

ONLY return valid JSON. No explanation. No markdown.

Format:
{{
  "modules": ["..."],
  "roles": ["..."],
  "features": ["..."]
}}

Input:
{user_input}
"""

    response = call_llm(prompt)

    data = extract_json(response)

    if data:
        return data
    else:
        return {
            "error": "Invalid JSON",
            "raw_output": response
        }