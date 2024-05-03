import streamlit as st
from pytube import YouTube
from pytube.exceptions import PytubeError
import os
import base64

def download_video(url, download_path):
    try:
        yt = YouTube(url)
        streams_with_audio = yt.streams.filter(file_extension='mp4', audio_codec='mp4a.40.2')
        stream = streams_with_audio.filter(res="720p").first()
        if stream:
            video_file_path = os.path.join(download_path, stream.default_filename)

            stream.download(output_path=download_path)
            return video_file_path
        else:
            return None
    except PytubeError as e:
        st.error(f"An error occurred: {e}")

def video_downloader():
    st.title("YouTube Video Downloader")

    entered_url = st.text_input("Enter the YouTube URL:", key="Video Input")
    if entered_url:
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        if st.button("Fetch Video"):
            with st.spinner("In Progress"):
                video_file_path = download_video(entered_url, download_path)  
            if video_file_path:
                with open(video_file_path, "rb") as f:
                    
                    video_bytes = f.read()
                video_b64 = base64.b64encode(video_bytes).decode()
                href = f'<a href="data:video/mp4;base64,{video_b64}" download="{os.path.basename(video_file_path)}" style="text-decoration: none; color: #fff; background-color: #007bff; padding: 8px 12px; border-radius: 4px;">Download</a>'
                st.markdown(href, unsafe_allow_html=True)


