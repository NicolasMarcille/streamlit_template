import streamlit as st
from lib.st_custom_components import st_audiorec

st.title("What's that language?")

wav_audio_data = st_audiorec()
temp_file = 'temp_file.wav'


if wav_audio_data is not None:
    # display audio data as received on the backend
    st.audio(wav_audio_data, format='audio/wav')

# INFO: by calling the function an instance of the audio recorder is created
# INFO: once a recording is completed, audio data will be saved to wav_audio_data




