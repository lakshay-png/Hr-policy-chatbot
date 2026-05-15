import streamlit as st

def login():

    st.title("🔐 HR Policy Chatbot Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.session_state.authenticated = True
        else:
            st.error("Invalid Credentials")