import streamlit as st
from main import run_pipeline
import json

st.set_page_config(page_title="AI App Generator", layout="wide")

st.title("🚀 AI App Generator")
st.write("Enter your idea and generate structured app configuration")

user_input = st.text_area("Describe your app")

if st.button("Generate App"):
    if not user_input:
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating..."):
            output = run_pipeline(user_input)

        st.success("Generated successfully!")

        # ---------------- JSON OUTPUT ----------------
        st.subheader("📦 Generated Configuration")
        st.json(output)

        # ---------------- UI PREVIEW ----------------
        st.subheader("🖥️ UI Preview")

        pages = output.get("ui", {}).get("pages", [])

        tab_names = [p["name"].capitalize() for p in pages]
        if tab_names:
            tabs = st.tabs(tab_names)

            for i, page in enumerate(pages):
                with tabs[i]:

                    if page["name"] == "login":
                        st.markdown("### 🔐 Login Page")
                        st.text_input("Email")
                        st.text_input("Password", type="password")
                        st.button("Login")

                    elif page["name"] == "dashboard":
                        st.markdown("### 📊 Dashboard")

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric("Total Contacts", "120", "+10%")
                        with col2:
                            st.metric("Revenue", "$50,000", "+8%")
                        with col3:
                            st.metric("Conversion Rate", "32%", "+5%")

                        st.markdown("#### 📈 Analytics")
                        st.line_chart([10, 20, 15, 30, 25])

                    elif page["name"] == "contacts":
                        st.markdown("### 👥 Contacts")

                        st.button("Add Contact")

                        st.table([
                            {"Name": "John", "Email": "john@gmail.com"},
                            {"Name": "Alice", "Email": "alice@gmail.com"}
                        ])

                    else:
                        st.markdown(f"### {page['name'].capitalize()} Page")
                        st.write("Preview not defined")

        # ---------------- DOWNLOAD ----------------
        st.download_button(
            label="Download JSON",
            data=json.dumps(output, indent=2),
            file_name="app_config.json",
            mime="application/json"
        )