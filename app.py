import streamlit as st
import os
from groq import Groq
from pypdf import PdfReader
import docx
from dotenv import load_dotenv

st.set_page_config(page_title="DocuSearch AI", page_icon="📄", layout="wide")

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("Add GROQ_API_KEY to .env or Streamlit secrets!")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

def load_document(uploaded_file):
    file_ext = uploaded_file.name.lower().split('.')[-1]

    if file_ext == 'txt':
        return uploaded_file.read().decode('utf-8').strip()

    elif file_ext == 'pdf':
        reader = PdfReader(uploaded_file)
        return "".join(page.extract_text() or "" for page in reader.pages).strip()

    elif file_ext == 'docx':
        doc = docx.Document(uploaded_file)
        return "\n".join(para.text for para in doc.paragraphs).strip()
    
    st.error(f"Unsupported: .{file_ext}")
    return None

def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    step = chunk_size - overlap
    chunks = []

    for i in range(0, len(words), step):
        chunk = words[i : i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks

def score_chunk(chunk, keywords):
    words = chunk.lower().split()
    words_set = set(words)

    overlap_scr = len(words_set.intersection(keywords))

    return overlap_scr

def get_best_chunk(chunks, question, min_score=2):
    question_words = question.lower().split()
    question_keywords = set(question_words)

    best_score, best_chunk = -1, None

    for chunk in chunks:
        score = score_chunk(chunk, question_keywords)

        if score > best_score:
            best_score, best_chunk = score, chunk

    return best_chunk if best_score >= min_score else None

def build_prompt(context, question):
    return f"""Context:
{context}

Question: {question}

Answer:"""

def get_answer_from_groq(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a Teacher who assists student in studying."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_completion_tokens=4096,
    )

    return response.choices[0].message.content.strip()

# Session State
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "document_text" not in st.session_state:
    st.session_state.document_text = None
if "chunks" not in st.session_state:
    st.session_state.chunks = []

# CSS
st.markdown("""
<style>
.main-title { font-size: 40px; font-weight: 700; }
.subtitle { font-size:18px; color:gray; margin-bottom:20px; }
.source-box { padding:15px; border-radius:10px; background:#f5f5f5; border:1px solid #ddd; }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="main-title">📄 DocuSearch AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask questions from your documents using AI</div>', unsafe_allow_html=True)
st.divider()

# SIDEBAR
with st.sidebar:
    st.title("⚙️ Controls")
    st.markdown("Upload a document and start asking questions.")
    
    uploaded_file = st.file_uploader("Upload Document", type=['txt','pdf','docx'])
    
    if uploaded_file:
        if st.session_state.uploaded_file != uploaded_file.name:
            # NEW FILE - PROCESS
            st.session_state.uploaded_file = uploaded_file.name
            st.session_state.document_text = load_document(uploaded_file)
            
            if st.session_state.document_text:
                st.session_state.chunks = chunk_text(st.session_state.document_text)
                st.success(f"✅ Loaded: {uploaded_file.name} ({len(st.session_state.chunks)} chunks)")
            else:
                st.error("❌ Failed to read document")
        
        if st.button("🧹 Clear Cache"):
            st.session_state.uploaded_file = None
            st.session_state.document_text = None
            st.session_state.chunks = []
            st.rerun()
    
    st.divider()
    st.markdown("### ℹ️ How it works")
    st.markdown("1. Upload a document\n2. Ask a question\n3. AI finds relevant context\n4. Generates an answer")

# MAIN CONTENT
if not st.session_state.uploaded_file:
    st.info("👈 Upload a document from the sidebar to begin.")
else:
    if st.session_state.document_text:
        question = st.chat_input("Ask something about the document...")
        
        if question:
            with st.chat_message("user"):
                st.markdown(question)
            
            with st.status("🔎 Searching document...", expanded=False):
                best_chunk = get_best_chunk(st.session_state.chunks, question, min_score=2)
            
            if best_chunk:
                with st.chat_message("assistant"):
                    with st.spinner("Generating answer..."):
                        prompt = build_prompt(best_chunk, question)
                        answer = get_answer_from_groq(prompt)
                        st.markdown(answer)
                
                with st.expander("📖 Source Context"):
                    st.markdown(f'<div class="source-box">{best_chunk[:1000]}...</div>', unsafe_allow_html=True)
            else:
                with st.chat_message("assistant"):
                    st.warning("❌ Couldn't find relevant context. Try rephrasing the question.")
    else:
        st.error("❌ Failed to read the document.")