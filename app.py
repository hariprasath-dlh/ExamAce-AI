import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def enhance_answer(student_answer, marks):
    if not api_key or api_key == "your_gemini_api_key_here":
        if int(marks) <= 5:
            return f"""# 👍 Good Answer on Generative AI (Marks: {marks})

Generative AI refers to algorithms and models (like neural networks) designed to generate new, original content based on patterns learned from existing data.

### Summary
Generative AI creates novel content by learning from data.
**Keywords:** `Artificial Intelligence`, `Content Generation`"""
        else:
            return f"""# 🚀 Excellent Answer on Generative AI (Marks: {marks})

**Generative AI** is a fascinating and rapidly evolving branch of artificial intelligence. Here is a structured version of your answer:

## What is Generative AI?
Generative AI refers to algorithms and models (like neural networks) designed to generate new, original content based on patterns learned from vast amounts of existing data. It can create text, images, audio, video, code, and more.

## Key Mechanisms
* **Foundation Models:** It relies on large-scale models (like LLMs) trained on vast amounts of unlabeled data.
* **Prompt Engineering:** Users guide the AI using natural language prompts to produce specific desired outputs.

### Summary
Generative AI is a powerful tool for creating novel content across various domains by learning from existing patterns.
**Keywords:** `Artificial Intelligence`, `Neural Networks`, `Foundation Models`, `Content Generation`"""
        
    prompt = f"""You are an expert university professor and exam evaluator.

Your task is to improve the given student answer based on the mark allocation.

Instructions:
- If marks are small (2–5): give a short, crisp answer with key points only
- If marks are medium (6–10): give a structured answer with headings and brief explanation
- If marks are high (11–20): give a detailed answer with headings, subheadings, examples, and depth

General rules:
- Use simple English
- Maintain clarity and logical flow
- Add important keywords

Also provide:
1. Improved answer (based on marks)
2. Important keywords
3. 2-line summary

Marks: {marks}
Student Answer:
{student_answer}"""

    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            generation_config=generation_config,
        )
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
         return f"Error: An error occurred while communicating with the AI. {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/enhance", methods=["POST"])
def enhance():
    data = request.json
    student_answer = data.get("answer", "").strip()
    marks = data.get("marks", "")
    
    if not student_answer:
        return jsonify({"error": "Student answer cannot be empty."}), 400
        
    if marks == "":
        return jsonify({"error": "Marks cannot be empty."}), 400
        
    try:
        marks_int = int(marks)
        if marks_int < 2 or marks_int > 20:
            return jsonify({"error": "Marks must be between 2 and 20."}), 400
    except ValueError:
        return jsonify({"error": "Invalid marks value."}), 400
        
    enhanced_content = enhance_answer(student_answer, marks_int)
    return jsonify({"enhanced_answer": enhanced_content})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
