import streamlit as st
from pytube import YouTube
from pytube.exceptions import PytubeError
import os

@st.cache_data()
def download_audio(url, download_path):
    try:
        yt = YouTube(url)
        audio_streams = yt.streams.filter(only_audio=True)
        # Choose the highest quality audio stream
        audio_stream = audio_streams.get_audio_only()
        if audio_stream:
            audio_stream.download(output_path=download_path)
            st.success("Audio download completed successfully!")
        else:
            st.error("No suitable audio stream found for download.")
    except PytubeError as e:
        st.error(f"An error occurred: {e}")

def audio_downloader():
    st.title("YouTube Audio Downloader")

    entered_url = st.text_input("Enter the YouTube URL:")
    if entered_url:
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        if st.button("Download Audio"):
            download_audio(entered_url, download_path)
