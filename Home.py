import streamlit as st
import openai
import importlib

# importlib.reload(utils)

openai.api_key = st.secrets['OPENAI_API_KEY']

# UI
st.title("What language is this?")

st.subheader("The ultimate language identification app")

st.markdown("#### Please click on the relevant side menu item")


