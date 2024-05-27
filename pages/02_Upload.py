import streamlit as st
from lib import utils
import pandas as pd

if 'df1' not in st.session_state:
    st.session_state.df1 = None

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.session_state.df1 = pd.read_csv(uploaded_file)

if st.session_state.df1 is not None:
    st.write(st.session_state.df1.head())
