import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Ensure GOOGLE_API_KEY is set in the .env file.")
    st.stop()

# Configure the Google Generative AI API with the API key
genai.configure(api_key=api_key)

# Initialize a chat session
session = genai.ChatSession(model="models/chat-bison-001")

def get_gemini_response(prompt):
    """Generates a response using the Gemini model through a chat session."""
    try:
        response = session.send_message(prompt)
        return response.get("candidates", [{}])[0].get("content", "No response generated.")
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Streamlit UI
st.title("GeminiDecode: Multilanguage Document Extraction")

uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    user_prompt = st.text_input("Enter your prompt:")
    if st.button("Tell me about the document"):
        if user_prompt:
            response = get_gemini_response(user_prompt)
            if response:
                st.write(f"Response: {response}")
        else:
            st.warning("Please enter a prompt.")
