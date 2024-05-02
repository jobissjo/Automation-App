import streamlit as st
import re
from nltk.corpus import stopwords



def remove_stopwords(text):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    # Reconstruct the text without stopwords
    filtered_text = ' '.join(filtered_words)
    return filtered_text

def remove_repeated_words(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Remove repeated words
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    # Reconstruct the text with unique words
    corrected_text = ' '.join(unique_words)
    return corrected_text

def note_taker():
    st.title("Text Correction")

    # Create a text area for inputting the text
    input_text = st.text_area("Enter your text here:", height=200)

    # Button to trigger text processing
    if st.button("Correct Sentence"):
        if input_text:
            # Remove stopwords
            text_without_stopwords = remove_stopwords(input_text)
            # Remove repeated words and correct text
            corrected_text = remove_repeated_words(text_without_stopwords)
            st.subheader("Corrected Text:")
            st.text_area(label="Corrected Text",value=corrected_text, height=10, label_visibility="collapsed")
        else:
            st.warning("Please enter some text.")


