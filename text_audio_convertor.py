import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO


def read_aloud(text: str):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang='en')
    tts.write_to_fp(mp3_fp)
    

    mp3_fp.seek(0)

    st.audio(mp3_fp, format='audio/mp3', start_time=0)


def download_audio(text: str):
    tts = gTTS(text, lang='en')
    with open('hello.mp3', 'wb') as f:
        tts.write_to_fp(f)
    
    # Read the saved file
    with open('hello.mp3', 'rb') as f:
        audio_content = f.read()

    # Base64 encode the audio content
    audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    # Create a link with download attribute
    href = f'<a href="data:audio/mpeg;base64,{audio_base64}" download="audio.mp3">Download</a>'
    
    # Display the link
    st.markdown(href, unsafe_allow_html=True)

def text_to_audio():
    st.title("Text to Audio")
    entered_text = st.text_area("Enter the text here")
    if st.button("Read Aloud", key='read_text_audio',use_container_width=False):
        read_aloud(entered_text)
    if st.button("Download Audio", key='download_text_audio'):
        download_audio(entered_text)

