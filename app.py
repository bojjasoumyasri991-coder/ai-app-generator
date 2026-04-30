import streamlit as st

st.set_page_config(page_title="AI System Generator", layout="wide")

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
.main-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 85vh;
}

.title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
}

.subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
    text-align: center;
}

.input-container {
    width: 60%;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# PIPELINE LOGIC
# -------------------------

def parse_prompt(prompt):
    prompt = prompt.lower()
    return {
        "auth": "login" in prompt,
        "contacts": "contact" in prompt,
        "dashboard": "dashboard" in prompt,
        "payments": "payment" in prompt or "premium" in prompt,
        "roles": "admin" in prompt or "role" in prompt,
        "analytics": "analytics" in prompt
    }


def build_system(features):
    system = {
        "UI Schema": {"pages": [], "components": []},
        "API Schema": {"endpoints": []},
        "Database Schema": {"tables": []},
        "Auth": {},
        "Business Logic": []
    }

    # UI
    if features["auth"]:
        system["UI Schema"]["pages"].append("Login Page")
    if features["dashboard"]:
        system["UI Schema"]["pages"].append("Dashboard Page")
    if features["contacts"]:
        system["UI Schema"]["pages"].append("Contacts Page")
    if features["payments"]:
        system["UI Schema"]["pages"].append("Subscription Page")
    if features["analytics"]:
        system["UI Schema"]["pages"].append("Admin Analytics Dashboard")

    system["UI Schema"]["components"] = ["Navbar", "Sidebar", "Forms", "Tables"]

    # API
    if features["auth"]:
        system["API Schema"]["endpoints"].append({"route": "/auth/login", "method": "POST"})

    if features["contacts"]:
        system["API Schema"]["endpoints"].extend([
            {"route": "/contacts", "method": "GET"},
            {"route": "/contacts", "method": "POST"},
            {"route": "/contacts/{id}", "method": "PUT"},
            {"route": "/contacts/{id}", "method": "DELETE"}
        ])

    if features["payments"]:
        system["API Schema"]["endpoints"].append(
            {"route": "/payment/checkout", "method": "POST"}
        )

    # Database
    if features["auth"]:
        system["Database Schema"]["tables"].append({
            "name": "Users",
            "fields": ["id", "email", "password", "role"]
        })

    if features["contacts"]:
        system["Database Schema"]["tables"].append({
            "name": "Contacts",
            "fields": ["id", "name", "email", "phone", "user_id"]
        })

    if features["payments"]:
        system["Database Schema"]["tables"].append({
            "name": "Subscriptions",
            "fields": ["id", "user_id", "plan", "status", "payment_id"]
        })

    # Auth
    if features["roles"]:
        system["Auth"] = {
            "roles": ["Admin", "User"],
            "permissions": {
                "Admin": "Full access + analytics",
                "User": "Limited access"
            }
        }

    # Business Logic
    if features["payments"]:
        system["Business Logic"].append("Only premium users can access advanced features")

    if features["roles"]:
        system["Business Logic"].append("Admin can view analytics dashboard")

    return system


def validate_system(system):
    if "Login Page" in system["UI Schema"]["pages"]:
        tables = [t["name"] for t in system["Database Schema"]["tables"]]
        if "Users" not in tables:
            system["Database Schema"]["tables"].append({
                "name": "Users",
                "fields": ["id", "email", "password"]
            })
    return system


# -------------------------
# UI
# -------------------------

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="title">🚀 AI System Generator</div>', unsafe_allow_html=True)

# ✅ FIXED SUBTITLE POSITION
st.markdown('<div class="subtitle">Turn your idea into full system architecture</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    user_input = st.text_area(
        "",
        placeholder="Build a CRM with login, contacts, dashboard, role-based access, premium plan with payments. Admins can see analytics.",
        height=120
    )

    generate = st.button("Generate System ➤", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# OUTPUT (FIXED)
# -------------------------

if "result" not in st.session_state:
    st.session_state.result = None

if generate:
    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else:
        features = parse_prompt(user_input)
        system = build_system(features)
        system = validate_system(system)
        st.session_state.result = system

if st.session_state.result:
    st.success("System generated successfully ✔")

    st.markdown("## 📦 Generated System Configuration")
    st.json(st.session_state.result)