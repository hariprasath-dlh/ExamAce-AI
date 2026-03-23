# 🚀 ExamAce AI – Smart Answer Enhancer

## 🧠 Overview
**ExamAce AI** is a Generative AI-powered web application that transforms raw student answers into structured, high-scoring exam responses. It intelligently adapts content based on mark allocation, helping students present answers effectively and improve academic performance.

---

## 🎯 Problem Statement
Many students understand concepts but struggle to present answers in a structured, exam-friendly format. This leads to loss of marks despite knowing the content.

---

## 💡 Solution
ExamAce AI enhances student answers using Generative AI by:
- Structuring content with headings and proper flow  
- Adding relevant keywords  
- Adjusting depth based on marks (2–20)  
- Improving clarity and readability  

---

## ✨ Key Features

- 📝 **Answer Enhancement**  
  Converts raw answers into well-structured exam-ready responses  

- 🎯 **Dynamic Mark-Based Generation**  
  - 2–5 marks → Short, crisp answers  
  - 6–10 marks → Structured explanations  
  - 11–20 marks → Detailed answers with depth  

- 🔑 **Keyword Booster**  
  Adds important exam keywords automatically  

- 📌 **Smart Summary**  
  Generates a quick 2-line revision summary  

- ⚡ **User-Friendly Interface**  
  Simple and clean UI for quick usage  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **AI Model:** OpenAI API / Google Gemini API  
- **Other Tools:** dotenv, REST API  

---

## ⚙️ How It Works

1. User enters a rough answer  
2. User selects the mark allocation  
3. AI processes input using a structured prompt  
4. Output generated:
   - Improved answer  
   - Keywords  
   - Summary  

---

## 📂 Project Structure

```
ExamAce-AI/
│── app.py
│── requirements.txt
│── .env
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/examace-ai.git
cd examace-ai
```

### 2. Create Virtual Environment (optional)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API Key
Create a `.env` file and add:

```env
OPENAI_API_KEY=your_api_key_here
```

or

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
python app.py
```

### 6. Open in Browser
```
http://127.0.0.1:5000
```

---

## 🧪 Sample Input & Output

### 🔹 Input
- Answer: *“Generative AI is a type of AI that creates content…”*  
- Marks: **5**

### 🔹 Output
- Short structured answer  
- Key points  
- Important keywords  
- Summary  

---

### 🔹 Input
- Same answer  
- Marks: **16**

### 🔹 Output
- Detailed explanation  
- Headings & subheadings  
- Expanded content  
- Keywords + summary  

---

## 📈 Future Enhancements

- 📄 PDF upload & summarization  
- 🎙️ Voice input support  
- 📊 Answer evaluation & scoring  
- 🌐 Multi-language support  

---

## 💼 Resume Value

This project demonstrates:
- Practical use of **Generative AI (NLP & NLG)**  
- Ability to build **real-world AI applications**  
- Understanding of **prompt engineering**  
- Full-stack development skills  

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and improve the project.

---

## ⭐ Support
If you like this project, don’t forget to ⭐ the repository!
