import streamlit as st
from lib import utils
from streamlit_extras.switch_page_button import switch_page


if 'language' not in st.session_state:
    st.session_state.language = ""


# UI starts
go_home = st.button("Home")
if go_home:
    switch_page("home")

st.title("What language is it?")

st.markdown("#### Enter text below:")

with st.form('form_text'):
    input_txt = st.text_area(label="", value="")
    submit = st.form_submit_button('Submit this')

response = ""
if submit:
    st.session_state.language = utils.find_language(input_txt)

if st.session_state.language:
    st.markdown("##### The language is:")
    st.markdown(f"### {st.session_state.language}")
