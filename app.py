from PIL import Image
import streamlit as st
import anthropic

st.title("AI VISION")

# Add input field for API key
api_key = st.text_input("Enter your Anthropoc API key:", type="password")

# Initialize Anthropoc client
client = None

if api_key:
    # Create an instance of the Anthropoc client
    client = anthropic.Anthropic(api_key=api_key)

# Input fields
input_text = st.text_input("Input Prompt:")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit = st.button("GO")

input_prompt = """
You are an expert in everything. We will upload an image,
and you will have to answer any questions based on the uploaded image.
"""

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# if submit button is clicked
if submit:
    if api_key and client:
        if uploaded_file:
            # Process the uploaded image and input
            bytes_data = uploaded_file.getvalue()
            image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]

            # Generate content using the "claude-3-sonnet-20240229" model
            message = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                temperature=0,
                messages=[input_text, image_parts[0], input_prompt]
            )
            st.subheader("The Response for Image:")
            st.write(message.content)
        else:
            st.error("No file uploaded")
    elif not api_key:
        st.error("Please enter your Anthropoc API key.")
    elif not client:
        st.error("Failed to initialize the Anthropoc client. Please check your API key.")
