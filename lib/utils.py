import openai
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

sd.default.channels = 1


def get_completion_from_messages(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response.choices[0].message["content"]


def create_frequency(frequency=440, seconds=1, fs=44100):
    t = np.linspace(0, seconds, seconds * fs, False)
    note = np.sin(frequency * t * 2 * np.pi)
    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    return audio


def play_audio(audio, fs=44100):
    sd.play(audio, fs)
    sd.wait()
    return 0


def record_audio(seconds: object = 10, fs: object = 44100) -> object:
    data = sd.rec(int(seconds * fs), samplerate=fs)
    sd.wait()
    data = data * (2 ** 15 - 1) / np.max(np.abs(data))
    data = data.astype(np.int16)
    return data


def save_audio(recording, filename='out.wav', fs=44100):
    write(filename, fs, recording)
    return 0

