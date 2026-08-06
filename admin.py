import streamlit as st
import pandas as pd

from database import *

def admin_dashboard():

    st.title("👨‍💼 Admin Dashboard")

    st.write("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Users", total_users())

    with col2:
        st.metric("High School", highschool_users())

    with col3:
        st.metric("Graduate", graduate_users())

    with col4:
        st.metric("Professional", professional_users())

    st.write("---")

    st.subheader("📋 Registered Users")

    users = get_users()

    if users:

        df = pd.DataFrame(
            users,
            columns=[
                "ID",
                "Username",
                "Email",
                "Category"
            ]
        )

        st.dataframe(df, width="stretch")

    else:

        st.info("No users found.")

    st.write("---")

    st.subheader("🔍 Search User")

    search = st.text_input("Enter Username")

    if st.button("Search", key="search_btn"):

        result = search_user(search)

        if result:

            df = pd.DataFrame(
                result,
                columns=[
                    "ID",
                    "Username",
                    "Email",
                    "Password",
                    "Category"
                ]
            )

            st.dataframe(df, width="stretch")

        else:

            st.error("User Not Found")

    st.write("---")

    st.subheader("❌ Delete User")

    delete = st.text_input(
        "Username to Delete",
        key="delete_user"
    )

    if st.button("Delete User", key="delete_btn"):

        delete_user(delete)

        st.success("User Deleted Successfully")

        st.rerun()

    st.write("---")


    if st.button("Logout", key="admin_logout"):

        st.session_state.logged_in = False
        st.session_state.role = "User"
        st.session_state.username = ""
        st.session_state.category = ""
        st.session_state.page = "Home"

        st.rerun()