# 📑 Social Media Content Analyzer

A lightweight Flask-based web app that lets you upload PDFs or images, extract text using OCR (Tesseract), and get simple readability analysis with word and sentence counts.

---

## ✨ Features
- 📄 **Upload Support**: Upload PDFs and image files (`.png`, `.jpg`, `.jpeg`)  
- 🔍 **Text Extraction**:  
  - PDF parsing with **PyPDF2**  
  - OCR extraction for images with **Tesseract**  
- 📊 **Basic Text Analysis**: Word count, sentence count, and readability suggestions  
- 🎨 **Frontend**:  
  - `static/css/style.css` → Stylesheet  
  - `static/js/script.js` → Client-side JS for interactivity  

---

## 🛠️ Tech Stack
- **Backend**: Python 3.12 (Flask)  
- **Text Extraction**: PyPDF2, pytesseract, Pillow  
- **OCR Engine**: Tesseract OCR  
- **Frontend**: HTML (Jinja templates), CSS, JavaScript  

---

## 📁 Project Structure
```bash
Social-Media-Content-Analyzer/
│
├── static/             
│   ├── css/
│   │   └── style.css       # Custom styles
│   ├── js/
│   │   └── script.js       # Client-side interactivity
│
├── templates/
│   └── index.html          # Main HTML page
│
├── uploads/                # Uploaded files
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python runtime version (3.12.3)
├── render.yaml             # Deployment config (Render)
└── README.md               # Documentation
⚙️ Installation & Setup
Prerequisites
Python 3.12+

Tesseract OCR installed on your system

1. Clone the Repository
bash
Copy code
git clone https://github.com/vishwas-anand/Social-Media-Content-Analyzer-.git
cd Social-Media-Content-Analyzer-
2. Setup Virtual Environment & Install Dependencies
bash
Copy code
# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Configure Tesseract Path
Make sure Tesseract is installed and accessible:

Windows (example path):

makefile
Copy code
C:\Program Files\Tesseract-OCR\tesseract.exe
Linux/Mac: usually installed at

bash
Copy code
/usr/bin/tesseract
If needed, update the path inside app.py when calling pytesseract.

4. Run the Application
bash
Copy code
python app.py
App runs at: http://127.0.0.1:5000

🎯 Usage

Open the app in your browser

Upload a PDF or image file

Extracted text and analysis (word & sentence count + recommendation) will be displayed

🚨 Note: Deployment not live due to server config issues.  
To test locally:
1. Clone repo
2. Install dependencies
3. Install Tesseract
4. Run `python app.py`

This project includes a render.yaml config for Render.
However, due to server issues with Tesseract installation, the hosted deployment is not currently live.

➡️ To test locally, please follow the installation steps above.

📝 Approach

I built a Flask-based web application that allows users to upload PDF and image files. The backend extracts text from PDFs using PyPDF2 and from images using Tesseract OCR with Pillow for preprocessing. After extraction, the text is analyzed with simple NLP-like steps such as word count and sentence detection. Based on the analysis, the app provides basic readability recommendations (e.g., add more detail, or simplify long sentences).

The frontend is minimal, built with HTML templates, a CSS stylesheet, and a small JavaScript file for handling file uploads and displaying results dynamically. I included basic error handling for empty uploads, unsupported formats, and missing files. The app stores files temporarily in an uploads folder for processing.

The goal was to keep the project simple, functional, and easy to run locally. It requires Python 3.12+, Tesseract OCR installed on the system, and dependencies listed in requirements.txt. Although Render deployment did not succeed due to OCR library installation issues, the application runs locally without issues.

This project demonstrates my ability to build a complete, end-to-end application within the time limit, focusing on problem-solving, clean code, and usability.
