import streamlit as st
from lib import utils
import sounddevice as sd
import numpy as np
import threading

sd.default.channels = 1
seconds = 3
fs = 44100

# Global variables
recording = False
data = []


def audio_callback(indata, frames, time, status):
    if recording:
        data.append(indata.copy())


def start_recording():
    with sd.InputStream(callback=audio_callback):
        sd.sleep(4000)


st.title("Audio Recording App")

if not recording and st.button("Start Recording"):
    recording = True
    data = []
    recording_thread = threading.Thread(target=start_recording)
    recording_thread.start()

if recording and st.button("Stop Recording"):
    recording = False
    st.experimental_rerun()

if data:
    st.audio(np.concatenate(data, axis=0), format="wav")
