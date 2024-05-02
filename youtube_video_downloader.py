import streamlit as st
from pytube import YouTube
from pytube.exceptions import PytubeError
import os

@st.cache_data()
def download_video(url, download_path):
    try:
        yt = YouTube(url)
        streams_with_audio = yt.streams.filter(file_extension='mp4', audio_codec='mp4a.40.2')
        # Choose the 720p video stream with audio
        stream = streams_with_audio.filter(res="720p").first()
        if stream:
            stream.download(output_path=download_path)
            st.success("Download completed successfully!")
        else:
            st.error("No suitable video stream found for download.")
    except PytubeError as e:
        st.error(f"An error occurred: {e}")

def video_downloader():
    st.title("YouTube Video Downloader")

    entered_url = st.text_input("Enter the YouTube URL:")
    if entered_url:
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        if st.button("Download"):
            download_video(entered_url, download_path)
