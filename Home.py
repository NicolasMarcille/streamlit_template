import streamlit as st
from st_custom_components import st_audiorec
from lib import utils
from streamlit_extras.switch_page_button import switch_page

# openai.api_key = st.secrets['OPENAI_API_KEY']

st.title("Identify the language")


if 'language' not in st.session_state:
    st.session_state.language = None

if 'transcript' not in st.session_state:
    st.session_state.transcript = None

st.markdown("#### Record voice and submit:")

with st.form('form_audio'):
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        with open('temp_file.wav', 'wb') as fp:
            fp.write(wav_audio_data)
    if st.form_submit_button('Submit this'):
        st.session_state.transcript = utils.transcribe_audio('temp_file.wav')
        print(st.session_state.transcript)
        st.session_state.language = utils.find_language(st.session_state.transcript)


if st.session_state.language is not None:
    st.markdown("##### The language is:")
    st.markdown(f"### {st.session_state.language}")

    st.markdown("##### The translation in English is:")
    st.markdown(f"### {utils.translate(st.session_state.transcript)}")


