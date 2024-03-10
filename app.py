from PIL import Image
import streamlit as st
import google.generativeai as genai

st.title("AI VISION")

# Add input field for API key
api_key = st.text_input("Enter your Google API key:", type="password")

# Initialize Gemini Pro Vision model
model = 'gemini-pro-vision'

if api_key:
    # Configure Gemini Pro Vision API with the provided API key
    genai.configure(api_key=api_key)
    
    # Load Gemini Pro Vision model
    model = genai.GenerativeModel('gemini-pro-vision')

# Input fields
input_text = st.text_input("Input Prompt:")
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
submit = st.button("GO")

input_prompt = """
You are an expert in everything. We will upload images ,
and you will have to answer any questions based on the uploaded  images.
Always make your responses detailed and well organized.
"""

# Display the uploaded images
if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# if submit button is clicked
if submit:
    if api_key and model:
        if uploaded_files:
            for uploaded_file in uploaded_files:
                # Process each uploaded image and input
                if uploaded_file is not None:
                    # Read the file into bytes
                    bytes_data = uploaded_file.getvalue()

                    image_parts = [
                        {
                            "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                            "data": bytes_data
                        }
                    ]

                    # Get response from Gemini Pro Vision API
                    response = model.generate_content([input_text, image_parts[0], input_prompt])
                    st.subheader("The Response for Image:")
                    st.write(response.text)
                else:
                    st.error("No file uploaded")
        else:
            st.error("No files uploaded. Please select one or more images.")
    elif not api_key:
        st.error("Please enter your Google API key.")
    elif not model:
        st.error("Failed to initialize the model. Please check your API key.")
