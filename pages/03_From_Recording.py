import streamlit as st
from st_custom_components import st_audiorec
from lib import utils


if 'language' not in st.session_state:
    st.session_state.language = ""

if 'transcript' not in st.session_state:
    st.session_state.transcript = ""


st.title("What's the language?")

st.markdown("#### Record voice amd submit")

with st.form('form_audio'):
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        with open('temp_file.wav', 'wb') as fp:
            fp.write(wav_audio_data)
    submit = st.form_submit_button('Submit this')

if submit:
    st.session_state.transcript = utils.transcribe_audio('temp_file.wav')
    st.session_state.language = utils.find_language(st.session_state.transcript)

if st.session_state.language:
    st.markdown("##### The language is:")
    st.markdown(f"### {st.session_state.language}")
