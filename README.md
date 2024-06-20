# resume_analyser

Sure! Below is a comprehensive `README.md` file for your GitHub repository:

```markdown
# Resume Analyzer with Generative AI and Streamlit

This project is a web application that allows users to upload a resume in PDF format, extract relevant information (Name, Education, Experience), and interact with a chatbot powered by Gemini AI. The chatbot provides job recommendations and insights based on the extracted resume information and user prompts.

## Features

- **PDF File Upload**: Upload resumes in PDF format.
- **Text Extraction**: Extract text from the uploaded PDF file.
- **Information Parsing**: Parse the extracted text to identify Name, Education, and Experience.
- **Chatbot Interaction**: Interact with a chatbot powered by Gemini AI to get job recommendations and insights.
- **Error Handling**: Display appropriate error messages for invalid file uploads or extraction errors.
- **Response Saving**: Save user prompts and AI-generated content to a JSON file.

## Technologies Used

- **Streamlit**: A web application framework for creating interactive applications.
- **Google Generative AI (Gemini API)**: An API for generating human-like text based on prompts.
- **PyMuPDF (Fitz)**: A PDF processing library used for extracting text from PDF files.
- **Regular Expressions (regex)**: For extracting specific information from the text.
- **Python Standard Libraries**: For various functionalities including file handling and environment variable management.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer
   ```

2. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root directory.
   - Add your Gemini API key to the `.env` file:
     ```env
     GEMINI_KEY=your_gemini_api_key
     ```

5. **Run the application**:
   ```sh
   streamlit run app.py
   ```

## Usage

1. **Upload Resume**:
   - Click on the "Upload PDF" button and select a resume file in PDF format.
   - The application will extract and display the Name, Education, and Experience from the resume.

2. **Interact with the Chatbot**:
   - Enter a natural language prompt in the input field.
   - Click on the "Process Content" button to generate AI responses.
   - The AI will provide job recommendations and insights based on the extracted resume information.

3. **View and Save Responses**:
   - The generated content will be displayed on the screen.
   - The prompt and generated content are saved to a JSON file for future reference.

## Example

![Example Screenshot](example.png)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Additional Notes:

1. **Replace Placeholders**: Ensure to replace placeholders such as `https://github.com/your-username/resume-analyzer.git` with the actual URL of your GitHub repository and `your_gemini_api_key` with your actual API key.

2. **Example Screenshot**: Include an example screenshot of your application in the repository and reference it in the README with `![Example Screenshot](example.png)`.

3. **License**: Include a `LICENSE` file in your repository if you want to specify the licensing terms.

4. **requirements.txt**: Ensure you have a `requirements.txt` file that lists all the dependencies required for your project. You can generate it with:
   ```sh
   pip freeze > requirements.txt
   ```

