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
    # Initialize Anthropic client with the provided API key
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
    if api_key and client:
        if uploaded_files:
            for uploaded_file in uploaded_files:
                # Process each uploaded image and input
                if uploaded_file is not None:
                    # Create message with Anthropic API
                    message = client.messages.create(
                        model="claude-3-sonnet-20240229",
                        max_tokens=1000,
                        temperature=0,
                        messages=[{
                            "data": uploaded_file,
                            "content_type": uploaded_file.type
                        }]
                    )
                    st.subheader("The Response for Image:")
                    st.write(message.content)
                else:
                    st.error("No file uploaded")
        else:
            st.error("No files uploaded. Please select one or more images.")
    elif not api_key:
        st.error("Please enter your Anthropics API key.")
    elif not client:
        st.error("Failed to initialize the Anthropic client. Please check your API key.")
