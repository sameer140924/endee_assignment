import streamlit as st
from pypdf import PdfReader
from transformers import pipeline
from utils.vector_store import EndeeVectorStore

vector_store = EndeeVectorStore()
qa_pipeline = pipeline("question-answering")

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_answer(context, question):
    result = qa_pipeline(question=question, context=context)
    return result["answer"]

st.title("📚 AI PDF Question Answering")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    text = extract_text(uploaded_file)
    chunks = text.split("\n\n")

    vector_store.clear_store()

    for chunk in chunks:
        if chunk.strip():
            vector_store.store_text(chunk)

    st.success("PDF Processed Successfully!")

query = st.text_input("Ask a question about the PDF")

if query:
    results = vector_store.search_similar(query)
    context = " ".join(results)
    answer = generate_answer(context, query)

    st.write("### Answer:")
    st.write(answer)
