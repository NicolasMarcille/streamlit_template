import streamlit as st
from lib import utils
import sounddevice as sd
import numpy as np
import threading
from time import sleep

sd.default.channels = 1
seconds = 5
fs = 44100

global data

if 'audio_data' not in st.session_state:
    st.session_state.audio_data = []


def task(event):
    global data
    data = sd.rec(int(seconds * fs), samplerate=fs)
    if event.is_set():
        sd.stop()
        return data
    else:
        sd.wait()
    return data


event = threading.Event()
thread = threading.Thread(target=task, args=(event,))

st.title("Audio Recording App")

status = st.empty()
status.text(st.session_state.audio_data)

start = st.button('Start Recording')
stop = st.button('Stop Recording')

if start:
    thread.start()
    data = data * (2 ** 15 - 1) / np.max(np.abs(data))
    data = data.astype(np.int16)
    st.write(data)

    if stop:
        event.set()

    thread.join()

status.text(st.session_state.audio_data)


if len(st.session_state.audio_data):
    st.audio(st.session_state.audio_data, sample_rate=fs)

