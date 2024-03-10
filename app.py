from PIL import Image
import streamlit as st
import anthropic
import base64


st.title("AI VISION")

# Add input field for API key
api_key = st.text_input("Enter your Anthropoc API key:", type="password")

# Initialize Anthropoc client
client = None

# Initialize Gemini Pro Vision model
model = None

if api_key:
    # Create an instance of the Anthropoc client
    client = anthropic.Anthropic(api_key=api_key)

# Input fields
input_text = st.text_input("Input Prompt:")
uploaded_files = st.file_uploader("Choose one or more images...", type=["jpg", "jpeg", "png"])
submit = st.button("GO")

input_prompt = """
You are an expert in everything. We will upload an image ,
and you will have to answer any questions based on the uploaded  image.
"""

# if submit button is clicked
if submit:
    if api_key and model:
        if uploaded_files:
            for uploaded_file in uploaded_files:
                # Process each uploaded image and input
                if uploaded_file is not None:
                    # Read the file into bytes
                    bytes_data = uploaded_file.getvalue()

                    # Base64 encode the image data
                    base64_data = base64.b64encode(bytes_data).decode('utf-8')

                    image_parts = [
                        {
                            "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                            "data": base64_data
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
