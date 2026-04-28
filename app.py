import streamlit as st
import json
from main import run_pipeline

st.set_page_config(page_title="AI App Generator", layout="wide")

# -------------------------------
# SESSION STATE SETUP
# -------------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "builder"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "output" not in st.session_state:
    st.session_state.output = None


# -------------------------------
# BUILDER MODE
# -------------------------------
if st.session_state.mode == "builder":

    st.title("🚀 AI App Generator")
    st.write("Enter your idea and generate structured app configuration")

    user_input = st.text_area("Describe your app")

    if st.button("Generate App"):

        if not user_input:
            st.warning("Please enter a prompt")
        else:
            with st.spinner("Generating..."):
                output = run_pipeline(user_input)
                st.session_state.output = output

    # Show output
    if st.session_state.output:

        st.subheader("📦 Generated Configuration")
        st.json(st.session_state.output)

        # Download button
        st.download_button(
            label="Download JSON",
            data=json.dumps(st.session_state.output, indent=2),
            file_name="app_config.json",
            mime="application/json"
        )

        st.divider()

        # -------------------------------
        # UI PREVIEW
        # -------------------------------
        st.subheader("🖥 UI Preview")

        pages = st.session_state.output.get("ui", {}).get("pages", [])

        page_names = [p["name"] for p in pages]

        selected_page = st.radio("Navigate", page_names, horizontal=True)

        for page in pages:
            if page["name"] == selected_page:

                st.header(f"{page['name'].capitalize()} Page")

                if page["name"] == "login":
                    st.text_input("Email")
                    st.text_input("Password", type="password")
                    st.button("Login")

                elif page["name"] == "contacts":
                    st.write("📋 Contacts Table")
                    st.button("Add Contact")

                elif page["name"] == "dashboard":
                    st.write("📊 Charts & Analytics")

        st.divider()

        # 🚀 LAUNCH APP BUTTON
        if st.button("🚀 Launch App"):
            st.session_state.mode = "app"
            st.rerun()


# -------------------------------
# APP MODE (REAL FLOW SIMULATION)
# -------------------------------
elif st.session_state.mode == "app":

    st.title("🖥 App Simulation")

    # -------------------------------
    # LOGIN SCREEN
    # -------------------------------
    if not st.session_state.logged_in:

        st.subheader("🔐 Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if email and password:

                # SIMPLE ROLE LOGIC
                if "admin" in email.lower():
                    st.session_state.role = "Admin"
                else:
                    st.session_state.role = "User"

                st.session_state.logged_in = True
                st.success(f"Logged in as {st.session_state.role}")
                st.rerun()
            else:
                st.error("Enter email and password")

    # -------------------------------
    # AFTER LOGIN
    # -------------------------------
    else:

        st.success(f"Welcome {st.session_state.role}")

        pages = st.session_state.output.get("ui", {}).get("pages", [])

        page_names = [p["name"] for p in pages]

        selected_page = st.sidebar.radio("Navigate", page_names)

        # -------------------------------
        # PAGE RENDERING
        # -------------------------------
        for page in pages:

            if page["name"] == selected_page:

                st.header(page["name"].capitalize())

                if page["name"] == "contacts":
                    st.write("📋 Contacts Table")
                    st.button("Add Contact")

                elif page["name"] == "dashboard":

                    # 🔒 ADMIN CHECK
                    if st.session_state.role != "Admin":
                        st.error("⛔ Access Denied: Admin only")
                    else:
                        st.write("📊 Admin Analytics Dashboard")

                elif page["name"] == "login":
                    st.info("Already logged in")

        st.divider()

        # LOGOUT
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.role = None
            st.session_state.mode = "builder"
            st.rerun()