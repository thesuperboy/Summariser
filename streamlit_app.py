import streamlit as st
from transformers import pipeline
st.title('Summaraiser')
txt = st.text_area('Text to summarise', ''' input your text
    ''')
classifier = pipeline("summarization")
if st.button('Summarise'):
    output = classifier(txt)
    st.write('Summarised:', output)
