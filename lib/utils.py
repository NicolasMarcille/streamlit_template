import numpy as np
from scipy.io.wavfile import write, read
from openai import OpenAI
client = OpenAI()

# sd.default.channels = 1


def get_completion_from_messages(messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format="text")
    return transcription


def find_language(text):
    delimiter = "###"
    system_message = f"""
    Your task is to identify the language in which the user input text is written. The user input text will be delimited
     by {delimiter}. Provide your answer with only one word, the name of the language. In the case where the input text is
     an empty string "", return also an empty string. If the language is uncertain give the most likely language based
     on the recognized words but add 'probably' in front. 
    """
    user_message = f"""
    In which natural language of the world is the following text {delimiter}{text}{delimiter}?
    """
    messages = [{'role': 'system', 'content': system_message},
                {'role': 'user', 'content': user_message}]

    response = get_completion_from_messages(messages)
    print(response)
    return response


def translate(text):
    system_message = f"""
        Your task is to translate the user input text into English. If it is already written in English, so keep the text as is.
         Otherwise translate it to English. Try to stay close to a literal translation. 
        """
    messages = [{'role': 'system', 'content': system_message},
                {'role': 'user', 'content': text}]

    response = get_completion_from_messages(messages)
    return response


def create_frequency(frequency=440, seconds=1, fs=44100):
    t = np.linspace(0, seconds, seconds * fs, False)
    note = np.sin(frequency * t * 2 * np.pi)
    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    return audio


def read_audio(filename):
    fs, wav = read(filename)
    return wav


def save_audio(recording, filename, fs=44100):
    write(filename, fs, recording)
    return 0


# import sounddevice
# def play_audio(audio, fs=44100):
#     sd.play(audio, fs)
#     sd.wait()
#     return 0
#
#
# def record_audio(seconds: object = 10, fs: object = 44100) -> object:
#     data = sd.rec(int(seconds * fs), samplerate=fs)
#     sd.wait()
#     data = data * (2 ** 15 - 1) / np.max(np.abs(data))
#     data = data.astype(np.int16)
#     return data
