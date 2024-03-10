import streamlit as st
import anthropic
import base64
import httpx

st.title("AI VISION")

# Add input field for API key
api_key = st.text_input("Enter your Anthropics API key:", type="password")

# Initialize Anthropics client
client = anthropic.Anthropic()

# Input fields
input_text = st.text_input("Input Prompt:")
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
submit = st.button("GO")

input_prompt = """
You are an expert in everything. We will upload images,
and you will have to answer any questions based on the uploaded images.
Always make your responses detailed and well organized.
"""

# Function to encode image to base64
def encode_image_to_base64(image_url):
    image_content = httpx.get(image_url).content
    image_base64 = base64.b64encode(image_content).decode("utf-8")
    return image_base64

# Send request when button is clicked
if submit:
    if api_key and input_text:
        if uploaded_files:
            for uploaded_file in uploaded_files:
                if uploaded_file is not None:
                    # Encode image to base64
                    image_data = base64.b64encode(uploaded_file.read()).decode("utf-8")

                    # Send request with image to Anthropics API
                    try:
                        message = client.messages.create(
                            model="claude-3-sonnet-20240229",
                            max_tokens=1024,
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {
                                            "type": "image",
                                            "source": {
                                                "type": "base64",
                                                "media_type": uploaded_file.type,
                                                "data": image_data,
                                            },
                                        },
                                        {
                                            "type": "text",
                                            "text": input_text
                                        }
                                    ],
                                }
                            ]
                        )
                        st.subheader("The Response for Image:")
                        st.write(message)
                    except Exception as e:
                        st.error(f"Error sending request: {e}")
                else:
                    st.error("No file uploaded")
        else:
            st.error("Please select one or more images.")
    else:
        st.error("Please enter your Anthropics API key and input prompt.")
