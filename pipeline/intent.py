import json
import re
from utils.llm import call_llm


# ---------------- JSON CLEANER ----------------
def extract_json(text: str):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass
    return None


# ---------------- NORMALIZER ----------------
def normalize_modules(modules):
    normalized = []

    for m in modules:
        m = m.lower().strip()

        if any(k in m for k in ["auth", "login", "authentication"]):
            normalized.append("login")

        elif any(k in m for k in ["contact", "crm"]):
            normalized.append("contacts")

        elif any(k in m for k in ["dashboard", "analytics"]):
            normalized.append("dashboard")

        elif any(k in m for k in ["payment", "premium", "subscription", "plan"]):
            normalized.append("payments")

        else:
            normalized.append(m)

    # remove duplicates
    normalized = list(set(normalized))

    # ensure core modules
    for core in ["login", "dashboard", "contacts"]:
        if core not in normalized:
            normalized.append(core)

    return normalized


# ---------------- MAIN FUNCTION ----------------
def extract_intent(user_input: str):

    prompt = f"""
You are a strict JSON generator.

Return ONLY valid JSON.

Format:
{{
  "modules": [],
  "roles": [],
  "features": []
}}

Input:
{user_input}
"""

    try:
        response = call_llm(prompt)
        data = extract_json(response)

        if data:
            modules = normalize_modules(data.get("modules", []))
            roles = data.get("roles", ["admin", "user"])
            features = data.get("features", [])

            # ✅ Ensure minimum modules
            if not modules:
                modules = ["login", "dashboard", "contacts"]

            return {
                "modules": modules,
                "roles": roles,
                "features": features
            }

    except Exception as e:
        print("LLM ERROR:", e)

    # ---------------- FALLBACK (VERY IMPORTANT) ----------------
    return {
        "modules": ["login", "dashboard", "contacts", "payments"],
        "roles": ["admin", "user"],
        "features": ["authentication", "crud", "analytics", "premium"]
    }