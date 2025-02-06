import streamlit as st
from nltk.corpus import wordnet
from nltk.stem.snowball import SnowballStemmer
import nltk

# Download WordNet data (only needed once)
nltk.download("wordnet")

# Initialize Stemmer
stemmer = SnowballStemmer("english")

def english_dict():
    st.title("Dictionary")

    entered_word = st.text_input("Enter the word")
    if entered_word:
        word = stemmer.stem(entered_word.strip())  # Stemming
        synsets = wordnet.synsets(word)  # Get word meanings

        if synsets:
            st.subheader(f"Definitions for '{entered_word}':")
            for i, syn in enumerate(synsets[:5]):  # Limit to first 5 meanings
                st.text(f"{i+1}. {syn.definition()}")
        else:
            st.subheader("No meaning found")
            st.text("Please check if you entered a valid word.")


