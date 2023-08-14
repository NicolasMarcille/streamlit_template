import streamlit as st
from lib import utils


# UI starts
st.title("What's that language?")


st.markdown("#### Enter text below:")
input_txt = st.text_area(label="", value="")

delimiter = "###"
system_message = f"""
Your task is to identify the language in which the user input text is written. The user input text will be delimited
 by {delimiter}. Provide your answer with only one word, the name of the language. In the case where the input text is
 an empty string "", return also an empty string. If the language is uncertain give the most likely language based
 on the recognized words 
"""

user_message = f"""
In which language is the following text {delimiter}{input_txt}{delimiter}?
"""
messages = [{'role': 'system', 'content': system_message},
            {'role': 'user', 'content': user_message}]

response = ""
if input_txt:
    response = utils.get_completion_from_messages(messages)

st.markdown("The language is:")
st.markdown(f"#### {response}")

