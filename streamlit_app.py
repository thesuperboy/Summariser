import streamlit as st
from transformers import pipeline
st.title('This is a title')
txt = st.text_area('Text to analyze', '''
    Input Your Text
    ''')
