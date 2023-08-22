import streamlit as st
from lib import utils
import sounddevice as sd
import numpy as np
import wavio


fs = 44100
sd.default.channels = 1

if 'audio' not in st.session_state:
    st.session_state.audio = []

record = st.button('Record 3 sec')


if record:
    audio = sd.rec(int(3 * fs), samplerate=fs)
    sd.wait()
    audio = audio * (2 ** 15 - 1) / np.max(np.abs(audio))
    audio = audio.astype(np.int16)
    st.session_state.audio = audio
    sd.play(st.session_state.audio, 44100)
    sd.wait()
    wavio.write("myfile.wav", st.session_state.audio, fs, sampwidth=2)

if len(st.session_state.audio) > 0:
    st.audio("myfile.wav")
