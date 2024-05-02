import os
import streamlit as st
from PIL import Image 
import pytesseract

st.title("Extract Text from image")
# Set the path to the Tesseract executable
TESSERACT_PATH = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
 

    
    # Function to upload image and extract text
def image_upload_and_button():
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Process Uploaded Image"):
        if uploaded_image is None:
            st.write("Please upload an image first.")
        else:
            # Open the uploaded image
            img = Image.open(uploaded_image)
            # Extract text from image using Tesseract
            text = pytesseract.image_to_string(img)
            # Display the extracted text
            st.subheader("Extracted Text:")
            st.text(text)





