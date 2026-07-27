import streamlit as st
from database import *

st.set_page_config(
    page_title="TalentSphere Elevate",
    page_icon="🧑‍💼",
    layout="wide",
)

# ------------------------------------------------------------------
# Brand palette
# ------------------------------------------------------------------
PRIMARY = "#6C5CE7"
PRIMARY_DARK = "#4B3FBF"
ADMIN_COLOR = "#EC4899"
CATEGORY_COLORS = {
    "High School Student": "#4AA3FF",
    "Graduate": "#12B76A",
    "Professional": "#F39C12",
}

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
# Styles
# -------------------------------

st.markdown(
    f"""
    <style>
        #MainMenu, footer {{visibility: hidden;}}
        .block-container {{ padding-top: 1.5rem; max-width: 1300px; }}
        html, body, [class*="css"] {{
            font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}

        .tse-banner {{
            background: linear-gradient(135deg, {PRIMARY} 0%, {PRIMARY_DARK} 100%);
            border-radius: 18px;
            padding: 1.8rem 2rem;
            margin-bottom: 1.2rem;
        }}
        .tse-title {{ font-size: 2.1rem; font-weight: 800; color: white; margin: 0; }}
        .tse-subtitle {{ font-size: 1rem; color: rgba(255,255,255,0.9); margin-top: 0.3rem; }}

        .status-badge {{
            display: inline-block;
            padding: 0.35rem 0.9rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            color: white;
        }}

        .tse-card {{
            background: white;
            border-radius: 14px;
            padding: 1.3rem 1.5rem;
            box-shadow: 0 2px 14px rgba(0,0,0,0.06);
            margin-bottom: 1rem;
        }}

        div.stButton > button {{ border-radius: 8px; font-weight: 600; }}
        div.stButton > button[kind="primary"] {{ background-color: {PRIMARY}; border: none; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# Header banner
# -------------------------------

if st.session_state.logged_in:
    if st.session_state.role == "Admin":
        badge_html = f'<span class="status-badge" style="background:{ADMIN_COLOR};">👨‍💼 Administrator</span>'
    else:
        cat = st.session_state.category or "User"
        color = CATEGORY_COLORS.get(cat, PRIMARY)
        badge_html = f'<span class="status-badge" style="background:{color};">👤 {st.session_state.username} · {cat or "No category selected"}</span>'
else:
    badge_html = '<span class="status-badge" style="background:rgba(255,255,255,0.2);">Not logged in</span>'

st.markdown(
    f"""
    <div class="tse-banner">
        <div class="tse-title">TalentSphere Elevate</div>
        <div class="tse-subtitle">AI Powered Career Guidance Platform</div>
        <div style="margin-top:0.8rem;">{badge_html}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# Navigation
# -------------------------------

col1, col2, col3, space, col4, col5 = st.columns([1, 1, 1, 1, 1, 1])

with col1:
    if st.button("🏠 Home", width="stretch"):
        st.session_state.page = "Home"

with col2:
    if st.button("ℹ️ About", width="stretch"):
        st.session_state.page = "About"

with col3:
    if st.button("📊 Dashboard", width="stretch"):
        st.session_state.page = "Dashboard"

# -------------------------------
# Login / Register
# -------------------------------

with col4:

    login = st.popover("👤 Login / Register", width="stretch")

    with login:

        st.markdown("#### Account Access")

        option = st.radio(
            "Select",
            ["Login", "Register"],
            horizontal=True,
        )

        st.divider()

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
                key="login_button",
                type="primary",
                width="stretch",
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
                key="register_button",
                type="primary",
                width="stretch",
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

    admin = st.popover("👨‍💼 Admin Login", width="stretch")

    with admin:

        st.markdown("#### Administrator Access")
        st.caption("Restricted to authorized platform administrators.")
        st.divider()

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
            key="admin_login_button",
            type="primary",
            width="stretch",
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

    home_col1, home_col2 = st.columns([1, 1])

    with home_col1:

        st.markdown('<div class="tse-card">', unsafe_allow_html=True)

        st.header("Welcome to TalentSphere Elevate")

        st.write("""
TalentSphere Elevate is an AI-powered career guidance platform designed for:

- High School Students
- Graduates
- Professionals

It helps users explore careers, improve skills, prepare for placements,
build resumes, and receive career guidance.
""")

        st.markdown('</div>', unsafe_allow_html=True)

    with home_col2:

        st.image(
            "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=900&q=80",
            width="stretch"
        )

# -------------------------------
# ABOUT PAGE
# -------------------------------

elif st.session_state.page == "About":

    st.markdown('<div class="tse-card">', unsafe_allow_html=True)

    st.header("About TalentSphere Elevate")

    st.subheader("Objectives")

    obj_col1, obj_col2 = st.columns(2)
    objectives = [
        ("🎯", "Career Guidance"),
        ("📄", "Resume Building"),
        ("💻", "Coding Practice"),
        ("🧑‍🏫", "Placement Preparation"),
        ("🤖", "AI Mentor Support"),
    ]
    for i, (icon, label) in enumerate(objectives):
        target = obj_col1 if i % 2 == 0 else obj_col2
        with target:
            st.markdown(
                f"""
                <div style="background:#F7F6FE; border-radius:10px; padding:0.7rem 1rem; margin-bottom:0.6rem;">
                    {icon} &nbsp; <b>{label}</b>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------
# DASHBOARD
# ---------------------------------

elif st.session_state.page == "Dashboard":

    if st.session_state.logged_in:

        st.markdown('<div class="tse-card">', unsafe_allow_html=True)

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

        if st.button("Continue", key="continue_button", type="primary"):

            st.session_state.category = category

            update_category(
                st.session_state.username,
                category
            )

            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

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