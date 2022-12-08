import streamlit as st
from transformers import pipeline
st.title('Summaraiser')
txt = st.text_area('Text to summarise', '''
    Input Your Text
    ''')
