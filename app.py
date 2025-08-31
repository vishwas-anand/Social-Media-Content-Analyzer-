import os
from flask import Flask, render_template, request, jsonify
import pytesseract
from PyPDF2 import PdfReader
from PIL import Image

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def extract_text(file_path):
    text = ""
    if file_path.lower().endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        text = pytesseract.image_to_string(Image.open(file_path))
    else:
        text = "Unsupported file format."
    return text.strip()

def analyze_text(text):
    if not text:
        return {"analysis": "No text found.", "recommendation": "Please upload a valid file."}

    # Simple word/sentence analysis
    word_count = len(text.split())
    sentence_count = text.count(".") + text.count("!") + text.count("?")

    analysis = f"Word Count: {word_count}, Sentences: {sentence_count}"
    recommendation = "Keep writing clearly. Try shorter sentences for better readability." if sentence_count > 5 else "Consider adding more detailed content."

    return {"analysis": analysis, "recommendation": recommendation}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        text = extract_text(file_path)
        result = analyze_text(text)

        return jsonify({"text": text, **result})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
