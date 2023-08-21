import streamlit as st
import sounddevice as sd
import soundfile as sf
import numpy as np
import queue
import tempfile
import sys

# Streamlit setup
st.title("Unlimited Audio Recorder")


# Argument parsing
def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text


# Streamlit UI elements
filename = st.text_input("Enter filename to save recording:", "output.wav")
device = st.selectbox("Select input device:", sd.query_devices(kind='input'))
samplerate = st.number_input("Enter sampling rate:", min_value=1000, value=44100)
channels = st.number_input("Enter number of channels:", min_value=1, value=1)
subtype = st.text_input("Enter sound file subtype (e.g., 'PCM_24'):")

# Queue for audio data
q = queue.Queue()


# Callback function for audio recording
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


# Recording logic
try:
    if samplerate is None:
        device_info = sd.query_devices(device['name'], 'input')
        samplerate = int(device_info['default_samplerate'])

    with sf.SoundFile(filename, mode='x', samplerate=samplerate,
                      channels=channels, subtype=subtype) as file:
        with sd.InputStream(samplerate=samplerate, device=device['name'],
                            channels=channels, callback=callback):
            st.write("#" * 80)
            st.write("Recording in progress...")
            st.write("#" * 80)
            st.write("Press Ctrl+C in the terminal to stop recording.")

            while True:
                file.write(q.get())

except KeyboardInterrupt:
    st.write("\nRecording finished: " + repr(filename))
except Exception as e:
    st.error(type(e).__name__ + ': ' + str(e))
