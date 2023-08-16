import streamlit as st
from lib.st_custom_components import st_audiorec


wav_audio_data = st_audiorec()


if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
