import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pytesseract
import pdfplumber
from PIL import Image
import google.generativeai as genai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
os.makedirs("uploads", exist_ok=True)

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise ValueError("❌ ERROR: GEMINI_API_KEY is not set in environment variables.")

genai.configure(api_key=GEMINI_KEY)

def generate_summary(text, length="short"):
    prompts = {
        "short": "Summarize this text in 2–3 concise sentences:\n\n",
        "medium": "Summarize this text in one clear paragraph:\n\n",
        "long": "Provide a detailed long summary with key points:\n\n"
    }
    prompt = prompts.get(length, prompts["short"]) + text

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Summarization Error: {str(e)}"

def extract_text_from_file(filepath):
    file = filepath.lower()

    # Extract text from PDF
    if file.endswith(".pdf"):
        try:
            text = ""
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            return text
        except Exception as e:
            return f"Error extracting text from PDF: {str(e)}"

    if file.endswith((".png", ".jpg", ".jpeg")):
        try:
            img = Image.open(filepath)
            return pytesseract.image_to_string(img)
        except Exception as e:
            return f"Error performing OCR on image: {str(e)}"

    return "Unsupported file type."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    length = request.form.get("length")

    if not file:
        return "No file uploaded."

    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)

    extracted_text = extract_text_from_file(path)
    summary = generate_summary(extracted_text, length)

    return render_template(
        "result.html",
        summary=summary,
        text=extracted_text,
        length=length.capitalize()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
