import streamlit as st
import openai

openai.api_key = st.secrets['OPENAI_API_KEY']

# UI
st.title("Nick's language identification app")

st.subheader("Choose the relevant page in the side menu")



