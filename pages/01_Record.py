import streamlit as st
from lib.whisper_stt import whisper_stt
from lib.utils import find_language, translate


text = whisper_stt(language='en')
# If you don't pass an API key, the function will attempt to retrieve it as an environment variable : 'OPENAI_API_KEY'.

if text:
    st.write(text)
    st.markdown("##### The language is:")
    st.markdown(f"### {find_language(text)}")

    st.markdown("##### The translation in English is:")
    st.markdown(f"### {translate(text)}")
