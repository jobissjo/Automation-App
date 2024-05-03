import streamlit as st
from pytube import YouTube
from pytube.exceptions import PytubeError
import os
import base64

def download_audio(url, download_path):
    try:
        yt = YouTube(url)
        audio_streams = yt.streams.filter(only_audio=True)
        # Choose the highest quality audio stream
        audio_stream = audio_streams.get_audio_only()
        if audio_stream:
            audio_file_path = os.path.join(download_path, audio_stream.default_filename)
            audio_stream.download(output_path=download_path)
            return audio_file_path
        else:
            return None
    except PytubeError as e:
        st.error(f"An error occurred: {e}")

def audio_downloader():
    st.title("YouTube Audio Downloader")

    entered_url = st.text_input("Enter the YouTube URL:", key="Audio Input")
    if entered_url:
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        if st.button("Fetch Audio"):
            with st.spinner("In Progress"):
                audio_file_path = download_audio(entered_url, download_path)
            if audio_file_path:
                with open(audio_file_path, "rb") as f:
                    audio_bytes = f.read()
                audio_b64 = base64.b64encode(audio_bytes).decode()
                href = f'<a href="data:audio/mpeg;base64,{audio_b64}" download="{os.path.basename(audio_file_path)}" style="text-decoration: none; color: #fff; background-color: #007bff; padding: 8px 12px; border-radius: 4px;">Download</a>'
                st.markdown(href, unsafe_allow_html=True)
