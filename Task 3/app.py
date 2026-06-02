import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv

from pdf_processor import extract_pdf_text
from rag_engine import split_document
from dashboard import (
    extract_dates,
    extract_stakeholders,
    extract_risks
)

load_dotenv()

genai.configure(
    api_key=os.getenv("AIzaSyB0KtA9hOQ6pLJJmDRORnAocc0_LicTcQ0")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

st.set_page_config(
    page_title="Knowledge Analyst RAG"
)

st.title("📚 Knowledge Analyst (RAG Concepts)")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_pdf_text(uploaded_file)

    st.success("PDF Loaded Successfully")

    st.subheader("Document Summary")

    summary_prompt = f"""
    Summarize this document:

    {text[:10000]}
    """

    summary = model.generate_content(
        summary_prompt
    )

    st.write(summary.text)

    st.subheader("Dashboard")

    dates = extract_dates(text)
    stakeholders = extract_stakeholders(text)
    risks = extract_risks(text)

    st.write("### Important Dates")
    st.write(dates)

    st.write("### Stakeholders")
    st.write(stakeholders)

    st.write("### Risks")
    st.write(risks)

    st.subheader("Ask Questions")

    question = st.text_input(
        "Enter Question"
    )

    if question:

        prompt = f"""
        Context:

        {text[:15000]}

        Question:

        {question}
        """

        response = model.generate_content(
            prompt
        )

        st.write("### Answer")
        st.write(response.text)