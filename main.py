import streamlit as st
st.set_page_config(page_title="Daily Task Helper", layout='wide')

from text_extraction import image_upload_and_button
from youtube_video_downloader import video_downloader
from youtube_audio_downloader import audio_downloader
from dictionary import english_dict
from note_taking import note_taker
from translator import tamil_translator
import nltk
from text_audio_convertor import text_to_audio
from streamlit_option_menu import option_menu


nltk.download('stopwords')



options = ["Extract Text from Image",   "Tamil Translator","Dictionary",
          "Youtube Videos", "Youtube Audios", "Text to Audio" ]


with st.sidebar:
    selected_option = option_menu(
        menu_title="Menu",
        options=options,
        icons=['file-earmark-image', 'translate', 
               'journal-bookmark-fill',
               'file-earmark-slides-fill', 'youtube', 'soundwave']
    )

# Display content based on selected option
if selected_option == "Extract Text from Image":
    image_upload_and_button()
elif selected_option == "Dictionary":
    english_dict()
# elif selected_option == "Note Taker":
#     note_taker()
elif selected_option == "Youtube Videos":
    video_downloader()
elif selected_option == "Youtube Audios":
    audio_downloader()
elif selected_option == "Tamil Translator":
    tamil_translator()
elif selected_option == "Text to Audio":
    text_to_audio()

