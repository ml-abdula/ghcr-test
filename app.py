import streamlit as st
import logger
st.set_page_config(page_title="GHCR test")
st.title("Hello from Streamlit in Docker")
name = st.text_input("Your name")
logger.info(f"User input: {name}")
st.write(f"Hi {name or 'there'}")

st.write(f"Ne wupdate")
