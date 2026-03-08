import streamlit as st

st.title("Test Deployment Web App")

name = st.text_input("Enter your full name")

if name:
    st.write("Welcome to the test project", name)