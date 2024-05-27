import streamlit as st
from lib.whisper_stt import whisper_stt
from lib.utils import find_language, translate
from streamlit_extras.switch_page_button import switch_page

# openai.api_key = st.secrets['OPENAI_API_KEY']

st.title("Audio peep")


if 'transcript' not in st.session_state:
    st.session_state.transcript = None

text = whisper_stt(start_prompt="Start",
                   stop_prompt="Stop",
                   use_container_width=True)
# If you don't pass an API key, the function will attempt to retrieve it as an environment variable : 'OPENAI_API_KEY'.

if text:
    st.session_state.transcript = text

    st.markdown("##### The language is:")
    st.markdown(f"### {find_language(text)}")

    st.markdown("##### The translation in English is:")
    st.markdown(f"### {translate(text)}")



