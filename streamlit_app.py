import streamlit as st
from transformers import pipeline
st.title('Summaraiser')
txt = st.text_area('Text to summarise', ''' input your text
    ''')
classifier = pipeline("summarization")
summarise = st.button("Summarise")
if summarise:
    output = classifier(txt)
    st.write('Summarised:', output)
