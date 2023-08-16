import streamlit as st
from lib import utils
import sounddevice as sd
import numpy as np
import threading
# from lib.st_custom_components import st_audiorec

sd.default.channels = 1
seconds = 3
fs = 44100
st.session_state.recording_thread = None
st.session_state.recording = False


def record_audio_fn():
    recording_data = sd.rec(int(seconds * fs), samplerate=fs)
    sd.wait()
    st.session_state.recording_data = recording_data


st.title("What's that language?")

status = st.empty()

if "recording" not in st.session_state:
    st.session_state.recording = False

if st.session_state.recording:
    if st.button("Stop Recording"):
        st.session_state.recording = False
        st.session_state.recording_thread.join()  # Wait for the recording thread to complete
    if "recording_data" in st.session_state:
        st.write(st.session_state.recording_data)
else:
    if st.button("Start Recording"):
        st.session_state.recording = True
        st.session_state.recording_thread = threading.Thread(target=record_audio_fn)
        st.session_state.recording_thread.start()


if st.button('Play'):
    if "recording_data" in st.session_state:
        record = st.session_state.recording_data
        record = record * (2 ** 15 - 1) / np.max(np.abs(record))
        record = record.astype(np.int16)
        utils.play_audio(record)



######
######

wav_audio_data = st_audiorec()

