import streamlit as st
from googletrans import Translator
import asyncio

async def translate_text(input_text):
    translator = Translator()
    # Perform translation asynchronously
    translated = await translator.translate(input_text, dest="ta")
    return translated.text

def tamil_translator():
    st.title("Tamil Translator")
    input_text = st.text_area("Enter the text here", height=150)

    if input_text:
        # Use asyncio to run the async translate function
        translated_text = asyncio.run(translate_text(input_text))
        st.text(translated_text)
