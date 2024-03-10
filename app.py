from dotenv import load_dotenv
from PIL import Image
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Input field for API key
api_key = st.text_input("Enter Google API Key:", key="api_key")

# Configure Google API key
if api_key:
    genai.configure(api_key=api_key)

# Load Gemini pro vision model
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, user_prompt):
    response = model.generate_content([input, image[0], user_prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
if api_key:
    st.set_page_config(page_title="MultiLanguage Invoice Extractor")

st.header("MultiLanguage Invoice Extractor")
input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit_button = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice
and you will have to answer any questions based on the uploaded invoice image
"""

# If submit button is clicked
if submit_button:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input_text)
    st.subheader("The Response is")
    st.write(response)
