from nltk.stem.snowball import SnowballStemmer
import streamlit as st
from PyDictionary import PyDictionary


stemmer = SnowballStemmer('english')
dictionary=PyDictionary()

def english_dict():
    st.title("Dictionar")
    
    entered_url = st.text_input("Enter the word")
    if entered_url:
        word = stemmer.stem(entered_url.strip())
        meaning = dictionary.meaning(word)
        if meaning:
            noun_meaning = meaning.get('Noun', '')
            verb_meaning = meaning.get('Verb', '')
            print(meaning)
            if noun_meaning:
                st.subheader("Noun Meaning:")
                for n in noun_meaning[:5]:
                    st.text(n)
            if verb_meaning:
                st.subheader("Verb Meaning:")
                for n in verb_meaning[:5]:
                    st.text(n)
        else:
            st.subheader("No Meaning found")
            st.text("Please check you entered a correct word, only enter a word")