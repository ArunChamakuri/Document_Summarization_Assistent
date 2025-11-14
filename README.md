# Document Summary Assistant

A web-based tool to summarize PDFs and images using Google Gemini AI. This application extracts text from documents and generates concise summaries in customizable lengths.

---

## Features

- Upload PDFs or images (`.png`, `.jpg`, `.jpeg`)  
- Extract text using **PDF parsing** (`pdfplumber`) and **OCR** (`pytesseract`)  
- Generate summaries in three lengths:  
  - **Short**: 2–3 sentences  
  - **Medium**: 1 paragraph  
  - **Long**: Detailed key points  
- Drag & drop interface or file selection  
- Display both the **extracted text** and **generated summary**  

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ArunChamakuri/Document_Summarization_Assistent.git
cd Document_Summarization_Assistent

2.**Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3.**Install dependencies:**
pip install -r requirements.txt
Install Tesseract OCR (required for image text extraction)
Windows: Download installer
macOS: brew install tesseract
Linux: sudo apt install tesseract-ocr

4.**Set Google Gemini API key**
export GEMINI_API_KEY="your_api_key_here"   # Linux/macOS
set GEMINI_API_KEY=your_api_key_here        # Windows

5.**Run the application:**
python app.py
Open your browser at http://127.0.0.1:5000/

__**Usage**__
Drag & drop your PDF or image or click to select a file.
Choose the summary length (short, medium, long).
Click Upload & Summarize.
View both the generated summary and original extracted text on the results page.
Click Upload Another Document to summarize a new file.

Project Structure
Document_Summarization_Assistent/
│
├─ app.py                 # Flask backend
├─ templates/
│  ├─ index.html          # Upload page
│  └─ result.html         # Summary display page
├─ static/
│  └─ style.css           # Stylesheet
├─ uploads/               # Folder for uploaded files (auto-created)
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation
