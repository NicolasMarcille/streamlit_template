import streamlit as st
from lib.whisper_stt import whisper_stt
from lib.utils import find_language, translate
from streamlit_extras.switch_page_button import switch_page

# openai.api_key = st.secrets['OPENAI_API_KEY']

st.title("Audio peep")

transcript = whisper_stt(start_prompt="START",
                         stop_prompt="STOP",
                         use_container_width=True)
# If you don't pass an API key, the function will attempt to retrieve it as
# an environment variable : 'OPENAI_API_KEY'.

if transcript:
    st.markdown(f"#### Translating from: {find_language(transcript.text)}")
    c = st.container(height=100, border=True)
    c.markdown(f"#### {translate(transcript.text)}")
