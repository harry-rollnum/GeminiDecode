import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# List models to see what's available
models = genai.list_models()
st.write("Available Models:", models)