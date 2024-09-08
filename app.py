import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os
#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
from PIL import Image

model = genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_response(input, images, prompt):
    response = model.generate_content([input, *images, prompt])  # Unpack images
    return response.text

def input_image_setup(uploaded_files):
    # Check if files have been uploaded
    if uploaded_files is not None:
        image_parts = []
        for uploaded_file in uploaded_files:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()
            image_parts.append(
                {
                    "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                    "data": bytes_data
                }
            )
        return image_parts
    else:
        raise FileNotFoundError("No files uploaded")

# Initializing Streamlit app
st.set_page_config(page_title="Automated Test Case Generator from Screenshots")

st.header("Automated Test Case Generator from Screenshots")
input = st.text_input("Context(Optional): ", key="input")

# Allow multiple images to be uploaded
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Display uploaded images
if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

submit = st.button("Tell me about the images")

# Input prompt for generating the test case
input_prompt = """
             I have a set of screenshots representing a digital product's feature, along with some optional context. Based on these screenshots and the provided context, I need you to generate a detailed step-by-step testing guide. For each feature shown in the screenshots, please provide the following information:

            1. Description: A brief summary of what the test case is about.
            2. Pre-conditions: Any requirements or setup steps that need to be completed before testing this feature.
            3. Testing Steps: Clear, numbered, step-by-step instructions on how to test the feature shown in the screenshot.
            4. Expected Result: The outcome I should expect if the feature is working correctly.
Please ensure that the instructions are clear and comprehensive for a tester. If there are multiple functionalities represented in the screenshots, break them down into separate test cases.
               """

# If the submit button is clicked
if submit:
    if uploaded_files:
        image_data = input_image_setup(uploaded_files)  # Process multiple images
        response = get_gemini_response(input, image_data, input_prompt)
        st.subheader("The Response is")
        st.write(response)
