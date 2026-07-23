import streamlit as st
from database import *

st.set_page_config(
    page_title="TalentSphere Elevate",
    layout="wide"
)

# -------------------------------
# Session State
# -------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = "User"

if "username" not in st.session_state:
    st.session_state.username = ""

if "category" not in st.session_state:
    st.session_state.category = ""

# -------------------------------
# Title
# -------------------------------

st.title("TalentSphere Elevate")

st.write("### AI Powered Career Guidance Platform")

st.divider()

# -------------------------------
# Navigation
# -------------------------------

col1, col2, col3, space, col4, col5 = st.columns([1,1,1,1,1,1])

with col1:
    if st.button("🏠 Home", width="stretch"):
        st.session_state.page = "Home"

with col2:
    if st.button("ℹ️About", width="stretch"):
        st.session_state.page = "About"

with col3:
    if st.button("📊 Dashboard", width="stretch"):
        st.session_state.page = "Dashboard"

# -------------------------------
# Login / Register
# -------------------------------

with col4:

    login = st.popover("👤 Login / Register")

    with login:

        option = st.radio(
            "Select",
            ["Login", "Register"]
        )

        # ---------------- LOGIN ----------------

        if option == "Login":

            username = st.text_input(
                "Username",
                key="login_user"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="login_pass"
            )

            if st.button(
                "Login",
                key="login_button"
            ):

                user = login_user(username, password)

                if user:

                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login Successful")

                    st.rerun()

                else:

                    st.error("Invalid Username or Password")

        # ---------------- REGISTER ----------------

        else:

            username = st.text_input(
                "Username",
                key="reg_user"
            )

            email = st.text_input(
                "Email",
                key="reg_email"
            )
            
            password = st.text_input(
                "Password",
                type="password",
                key="reg_pass"
            )

            if st.button(
                "Register",
                key="register_button"
            ):
                

                if register_user(
                    username,
                    email,
                    password
                ):

                    st.success("Registration Successful")

                else:

                    st.error("Username Already Exists")

# -------------------------------
# Admin Login
# -------------------------------

with col5:

    admin = st.popover("👨‍💼 Admin Login")

    with admin:

        admin_user = st.text_input(
            "Admin Username",
            key="admin_user"
        )

        admin_pass = st.text_input(
            "Admin Password",
            type="password",
            key="admin_pass"
        )

        if st.button(
            "Login as Admin",
            key="admin_login_button"
        ):

            if admin_user == "admin" and admin_pass == "admin123":

                st.session_state.logged_in = True
                st.session_state.role = "Admin"
                st.session_state.username = "Administrator"

                st.success("Welcome Administrator")

                st.rerun()

            else:

                st.error("Invalid Admin Credentials")

# -------------------------------
# HOME PAGE
# -------------------------------

if st.session_state.page == "Home":

    st.header("Welcome to TalentSphere Elevate")

    st.write("""
TalentSphere Elevate is an AI-powered career guidance platform designed for:

- High School Students
- Graduates
- Professionals

It helps users explore careers, improve skills, prepare for placements,
build resumes, and receive career guidance.
""")

# -------------------------------
# ABOUT PAGE
# -------------------------------

elif st.session_state.page == "About":

    st.header("About TalentSphere Elevate")

    st.subheader("Objectives")

    st.write("""
✔ Career Guidance

✔ Resume Building

✔ Coding Practice

✔ Placement Preparation

✔ AI Mentor Support
""")
# ---------------------------------
# DASHBOARD
# ---------------------------------

elif st.session_state.page == "Dashboard":

    if st.session_state.logged_in:

        st.header("📊 User Dashboard")

        st.success(f"Welcome, {st.session_state.username}")

        st.write("### Select Your Category")

        category = st.radio(
            "Choose One",
            [
                "High School Student",
                "Graduate",
                "Professional"
            ]
        )

        if st.button("Continue", key="continue_button"):

            st.session_state.category = category

            update_category(
                st.session_state.username,
                category
            )

            st.rerun()

        st.divider()

        if st.button("Logout", key="logout_button"):

            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.role = "User"
            st.session_state.category = ""
            st.session_state.page = "Home"

            st.rerun()

    else:

        st.warning("Please Login First")
    
    # ---------------------------------
# OPEN DASHBOARDS
# ---------------------------------

if st.session_state.logged_in:
    if st.session_state.role == "Admin":
        from admin import admin_dashboard
        admin_dashboard()

    elif st.session_state.category == "High School Student":

        from highschool import highschool_dashboard

        highschool_dashboard()

    elif st.session_state.category == "Graduate":

        from graduate import graduate_dashboard

        graduate_dashboard()

    elif st.session_state.category == "Professional":

        from professional import professional_dashboard

        professional_dashboard()