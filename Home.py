import streamlit as st
import openai
from streamlit_extras.switch_page_button import switch_page


openai.api_key = st.secrets['OPENAI_API_KEY']

# UI
st.title("What language is it?")

st.markdown("#### The ultimate lightweight language identification app")

goto_text = st.button("From text input")
goto_audio = st.button("From audio input")

if goto_text:
    switch_page("from text")

if goto_audio:
    switch_page("from recording")
