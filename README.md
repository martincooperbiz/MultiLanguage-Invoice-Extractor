# MultiLanguage Invoice Extractor 💼🔍

MultiLanguage Invoice Extractor is a Streamlit application designed to extract information from invoices using Google Gemini Pro Vision AI. Users can upload an image of an invoice, input a prompt, and receive detailed responses about the invoice content.

## 📝 Features

- **Invoice Analysis**: Users can upload an image of an invoice and input a prompt to extract information.
- **Gemini Pro Vision AI**: The application utilizes Google Gemini Pro Vision AI to analyze the uploaded invoice image and provide detailed responses.
- **MultiLanguage Support**: Supports analyzing invoices in multiple languages, thanks to the powerful capabilities of Gemini Pro Vision AI.

## 🚀 Getting Started

To run the MultiLanguage Invoice Extractor locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up your Google API key and other environment variables as specified in the `.env` file.
4. Run the Streamlit app by executing `streamlit run app.py` in your terminal.

## 💡 Usage

1. Input your prompt in the provided text input field.
2. Choose an image of the invoice by clicking on the file uploader button.
3. Click on the "Tell me about the invoice" button to generate a response based on the uploaded invoice image and input prompt.
4. View the detailed response provided by the Gemini Pro Vision AI.

## 🛠️ Technologies Used

- **Streamlit**: For building the interactive web application.
- **Google Gemini Pro Vision AI**: For analyzing invoice images and providing detailed responses.
- **PIL (Python Imaging Library)**: For handling image files.
- **dotenv**: For loading environment variables.

## 🙏 Acknowledgements

Special thanks to Google Generative AI for providing access to the Gemini Pro Vision AI.
