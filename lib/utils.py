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
