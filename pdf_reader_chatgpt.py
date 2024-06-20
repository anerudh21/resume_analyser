import streamlit as st
import fitz
import re
import io
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_KEY")

# Function to read PDF file
def read_pdf_file(uploaded_file):
    try:
        with io.BytesIO(uploaded_file.read()) as file_buffer:
            doc = fitz.open(stream=file_buffer, filetype="pdf")
            text = ""
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text += page.get_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

# Function to generate content using Generative AI model
def generate_content(data, user_prompt):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"{data}\n{user_prompt}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None

# Function to parse resume text
def parse_resume_text(text):
    resumes = {}
    name_pattern = re.compile(r"Name:\s*(.*)")
    experience_pattern = re.compile(r"Experience:\s*(.*)", re.IGNORECASE)
    education_pattern = re.compile(r"Education:\s*(.*)", re.IGNORECASE)
    individuals = text.split("\n\n")

    for individual in individuals:
        name_match = name_pattern.search(individual)
        experience_match = experience_pattern.search(individual)
        education_match = education_pattern.search(individual)

        if name_match:
            name = name_match.group(1).strip()
            experience = experience_match.group(1).strip() if experience_match else ""
            education = education_match.group(1).strip() if education_match else ""

            resumes[name] = {"Experience": experience, "Education": education}

    return resumes

# Streamlit app
def main():
    st.title("Resume Analyzer")

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        if uploaded_file.type != "application/pdf":
            st.error("Only PDF files are supported. Upload different file")
            return

        resume_text = read_pdf_file(uploaded_file)
        if resume_text:
            st.success("PDF Loaded Successfully")
        else:
            st.error("Failed to Load PDF")
            return

        # Get user prompt
        user_prompt = st.text_input("Enter your prompt:")

        # Process content
        if st.button("Process Content"):
            content = generate_content(resume_text, user_prompt)
            if content:
                parsed_data = parse_resume_text(resume_text)
                for name, details in parsed_data.items():
                    st.write(f"Name: {name}")
                    st.write(f"Experience: {details['Experience']}")
                    st.write(f"Education: {details['Education']}")
                    st.write("\n")

                st.write("Generated Content:")
                st.write(content)

                # Save prompt and content to JSON file
                prompt_response = {
                    "Prompt": user_prompt,
                    "Generated_Content": content
                }

                with open('prompt_responses.json', 'a') as json_file:
                    json.dump(prompt_response, json_file)
                    json_file.write('\n')
            else:
                st.error("Failed to generate content")

if __name__ == "__main__":
    main()
