from deep_translator import GoogleTranslator
import streamlit as st


def tamil_translator():
    st.title("Tamil Translator")
    input_text = st.text_area("Enter the text here", height=10)
    translated = GoogleTranslator(source='auto', target='ta').translate(input_text)
    print(translated)
    st.text(translated)