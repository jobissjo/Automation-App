import streamlit as st
st.set_page_config(page_title="Task Master", layout='wide')

from text_extraction import image_upload_and_button
from youtube_video_downloader import video_downloader
from youtube_audio_downloader import audio_downloader
from todo import todo_list
from dictionary import english_dict
from note_taking import note_taker
from translator import tamil_translator
import nltk

nltk.download('stopwords')

# Define sidebar options
options = ["Extract Text from Image", "Dictionary", "Note Taker", "Youtube Videos", "Youtube Audios", "To Do", "Tamil Translator"]

# Display sidebar options line by line
with st.sidebar:
    st.header("Side bar")
    selected_option = st.sidebar.radio("select Option", options, label_visibility="collapsed")

# Display content based on selected option
if selected_option == "Extract Text from Image":
    image_upload_and_button()
elif selected_option == "Dictionary":
    english_dict()
elif selected_option == "Note Taker":
    note_taker()
elif selected_option == "Youtube Videos":
    video_downloader()
elif selected_option == "Youtube Audios":
    audio_downloader()
elif selected_option == "To Do":
    todo_list()
elif selected_option == "Tamil Translator":
    tamil_translator()
