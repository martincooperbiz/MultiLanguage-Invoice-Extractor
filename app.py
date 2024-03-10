import streamlit as st
import anthropic
import base64
import httpx

st.title("AI VISION")

# Add input field for API key
api_key = st.text_input("Enter your Anthropics API key:", type="password")

# Initialize Anthropics client
client = anthropic.Anthropic(api_key=api_key)

# Input field for prompt text
input_text = st.text_input("Input Prompt:")

# File uploader for images
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Button to trigger processing
submit = st.button("Process Images")

# Display uploaded images
if uploaded_files:
    st.subheader("Uploaded Images:")
    for uploaded_file in uploaded_files:
        st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)

# Function to encode image to base64
def encode_image_to_base64(image_file):
    image_content = image_file.read()
    image_base64 = base64.b64encode(image_content).decode("utf-8")
    return image_base64

# Send request when button is clicked
if submit:
    if api_key and input_text:
        if uploaded_files:
            try:
                messages = []
                for uploaded_file in uploaded_files:
                    if uploaded_file is not None:
                        # Encode image to base64
                        image_data = encode_image_to_base64(uploaded_file)

                        # Add image and text to messages
                        messages.append({
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
                            ]
                        })

                # Send request with images to Anthropics API
                response = client.messages.create(
                    model="claude-3-opus-20240229",
                    max_tokens=1024,
                    messages=messages
                )

                st.subheader("The Response for Images:")
                st.write(response)

            except Exception as e:
                st.error(f"Error sending request: {e}")

        else:
            st.error("Please select one or more images.")
    else:
        st.error("Please enter your Anthropics API key and input prompt.")
