from PIL import Image

import streamlit as st

import google.generativeai as genai

st.title("MultiLanguage Invoice Extractor")

# Add input field for API key
api_key = st.text_input("Enter your Google API key:", type="password")

# Initialize Gemini Pro Vision model
model = None

if api_key:
    # Configure Gemini Pro Vision API with the provided API key
    genai.configure(api_key=api_key)
    
    # Load Gemini Pro Vision model
    model = genai.GenerativeModel('gemini-pro-vision')

# Input fields
input_text = st.text_input("Input Prompt:")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in everything. We will upload an image ,
and you will have to answer any questions based on the uploaded  image.
"""

# if submit button is clicked
if submit:
    if api_key and model:
        # Process image and input
        if uploaded_file is not None:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()

            image_parts = [
                {
                    "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]
        else:
            st.error("No file uploaded")
            st.stop()

        # Get response from Gemini Pro Vision API
        response = model.generate_content([input_text, image_parts[0], input_prompt])
        st.subheader("The Response is")
        st.write(response.text)
    elif not api_key:
        st.error("Please enter your Google API key.")
    elif not model:
        st.error("Failed to initialize the model. Please check your API key.")
