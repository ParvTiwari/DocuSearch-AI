# 📄 DocuSearch AI

AI-powered document Q&A system — upload PDFs, DOCX, and TXT files to get instant answers from your study materials.

## 🧩 Problem

Students and developers often struggle to efficiently extract useful information from large documents like research papers, notes, and technical documentation.

Traditional search (Ctrl+F) fails when:

- The query is semantic (not exact keyword match)
- Information is spread across multiple sections
- Context is required to understand answers

👉 **Goal:** Build a fast, lightweight system that enables natural language querying over personal documents.

---

## 💡 Approach

This project implements a **lightweight RAG (Retrieval-Augmented Generation)** pipeline:

### 1. Document Parsing
- Extract text from PDF, DOCX, and TXT files

### 2. Chunking Strategy
- Split text into ~300-word chunks with overlap  
- Preserves context across boundaries  

### 3. Retrieval Layer
- Keyword-based scoring system  
- Filters chunks with minimum relevance threshold (≥ 2 matches)  

### 4. Generation Layer
- Selected context passed to Groq Llama-3.3-70B  
- Generates accurate, context-grounded answers  

### 5. UI Layer
- Built with Streamlit for simplicity and fast deployment  

---

## 🔁 Iterations

- **V1:** Basic document upload + full text search  
- **V2:** Added chunking to improve retrieval accuracy  
- **V3:** Introduced keyword scoring + filtering (reduced noise)  
- **V4:** Integrated Groq LLM for fast inference  
- **V5:** Added source context display for answer verification  
- **V6 (Current):** Optimized chunk size & overlap for better recall

---

## ⚙️ Key Design Decisions

### 🔹 Keyword-based retrieval instead of embeddings
- Faster, simpler, no heavy infrastructure  
- Trade-off: lower semantic understanding  

### 🔹 Chunk size (~300 words)
- Balances context richness and retrieval precision  

### 🔹 Minimum relevance threshold (≥ 2 matches)
- Reduces hallucinations by filtering weak matches  

### 🔹 Groq LLM over OpenAI
- Much faster inference  
- Better real-time user experience  

### 🔹 Streamlit UI
- Rapid prototyping and deployment  
- Minimal frontend overhead  

---

## ⏱️ Daily Time Commitment

- Average: **2–3 hours/day**  
- Total duration: **~10–12 days**

### 📊 Breakdown

- Core logic & RAG pipeline: 5 days  
- UI & integration: 3 days  
- Improvements: 2–4 days  

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
git clone https://github.com/ParvTiwari/DocuSearch-AI.git
cd docusearch-ai
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

## 🛠️ Tech Stack

```text
Frontend: Streamlit
AI: Groq API (Llama-3.3-70B-Versatile)
Document Processing: PyPDF, python-docx
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
- [PyPDF](https://pypi.org/project/PyPDF2/) — PDF processing
- [python-docx](https://pypi.org/project/python-docx/) — DOCX support

Built for students by students 🚀

**Ask your documents anything!**
