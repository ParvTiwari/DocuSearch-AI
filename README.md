# 📄 DocuSearch AI

AI-powered document Q&A system — upload PDFs, DOCX, and TXT files to get instant answers from your study materials.

## ✨ Features

- 📚 **Multi-format support:** PDF, DOCX, TXT files
- 🎯 **Smart retrieval:** Keyword-based chunking with overlap
- 🤖 **AI answers:** Groq Llama-3.3-70B (ultra-fast inference)
- ✅ **Relevance filtering:** Minimum 2 keyword matches required
- 📖 **Source verification:** View exact context used for answers
- ⚙️ **Production ready:** Session state, error handling, clean UI

## 🎓 Perfect For

- Research papers & academic documents
- Lecture notes & study materials
- Internship documents & resumes
- Code documentation & technical specs
- Technical reports & manuals

## 🚀 Quick Start

```bash
# Clone & install
git clone https://github.com/ParvTiwari/DocuSearch.git
cd docusearch
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

## 🛠️ Tech Stack

```text
Frontend: Streamlit
AI: Groq API (Llama-3.3-70B-Versatile)
Document Processing: PyPDF2, python-docx
Retrieval: Custom keyword-based RAG
Deployment: Streamlit Cloud
```

## 📁 File Structure

```text
docusearch/
├── app.py             # Main Streamlit app
├── requirements.txt   # Dependencies
├── .gitignore         # Git exclusions
└── README.md          # You're reading it!
```

## 🎯 How It Works

```text
1. Upload  → PDF/DOCX/TXT processed into 300-word chunks
2. Query   → Keyword matching finds best chunk (score ≥ 2)
3. RAG     → Context + question sent to Groq Llama-3.3
4. Answer  → AI generates precise response with source context
```

## 🔑 Get Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:

   ```bash
   streamlit run app.py
   ```

3. Upload your documents and start asking questions.

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/) — Amazing web UI framework
- [Groq](https://groq.com/) — Lightning-fast AI inference
- [PyPDF2](https://pypi.org/project/PyPDF2/) — PDF processing
- [python-docx](https://pypi.org/project/python-docx/) — DOCX support

Built for students by students 🚀

**Ask your documents anything!**
