from dotenv import load_dotenv
load_dotenv()  # loading all environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        # Provide a default text if input is empty
        response = model.generate_content(["Describe this image", image])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="TextSnap")
st.header("Image Analyzer")

input_text = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me about the Image")

# If submit button is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("Content in the Image:")
    st.write(response)
