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

# Function to encode image to base64
def encode_image_to_base64(image_file):
    image_content = image_file.read()
    image_base64 = base64.b64encode(image_content).decode("utf-8")
    return image_base64

# Function to display response
def display_response(response):
    st.subheader("Response for Images:")
    st.markdown(f"**Message ID:** `{response['id']}`")
    st.markdown(f"**Model:** `{response['model']}`")
    st.markdown(f"**Role:** `{response['role']}`")
    st.markdown(f"**Stop Reason:** `{response['stop_reason']}`")
    st.markdown(f"**Stop Sequence:** {response['stop_sequence']}")
    
    st.markdown("**Content:**")
    st.write(response['content'][0]['text'])  # Displaying content
    
    st.markdown("**Usage:**")
    st.markdown(f"- **Input Tokens:** {response['usage']['input_tokens']}")
    st.markdown(f"- **Output Tokens:** {response['usage']['output_tokens']}")

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

                display_response(response)

            except Exception as e:
                st.error(f"Error sending request: {e}")

        else:
            st.error("Please select one or more images.")
    else:
        st.error("Please enter your Anthropics API key and input prompt.")
