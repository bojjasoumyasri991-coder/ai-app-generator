import streamlit as st
from main import run_pipeline
import json

st.set_page_config(page_title="AI App Generator", layout="wide")

st.title("🚀 AI App Generator")
st.write("Enter your idea and generate structured app configuration")

user_input = st.text_area("Describe your app", height=150)

if st.button("Generate App"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating..."):
            output = run_pipeline(user_input)

        st.subheader("📦 Generated Configuration")
        st.json(output)

        # Optional: download button
        st.download_button(
            label="Download JSON",
            data=json.dumps(output, indent=2),
            file_name="app_config.json",
            mime="application/json"
        )