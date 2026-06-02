# Knowledge Analyst (RAG Concepts)

## Overview

Knowledge Analyst is a Retrieval-Augmented Generation (RAG) application developed as part of the DecodeLabs Generative AI Internship Program.

The project enables users to upload PDF documents, generate summaries, identify risks, extract important dates and stakeholders, and ask questions based on document content using Google's Gemini AI model.

## Project Objective

The objective of this project is to simulate a document intelligence system capable of analyzing large documents and providing accurate, context-aware responses.

## Features

### PDF Processing

- Upload PDF documents
- Extract document text
- Handle multi-page files

### AI-Powered Summarization

- Generate concise document summaries
- Highlight key information
- Improve document understanding

### Risk Analysis

- Identify potential risks
- Detect liability-related content
- Highlight compliance concerns

### Date Extraction

- Detect important dates
- Identify deadlines and milestones

### Stakeholder Detection

- Extract relevant stakeholders
- Identify parties involved in the document

### Question Answering

- Ask questions about uploaded documents
- Receive context-aware responses
- Improve document accessibility

## Technology Stack

### Frontend

- Streamlit

### Backend

- Python

### AI Models

- Google Gemini

### Libraries

- LangChain
- FAISS
- PyPDF
- Python Dotenv

## Project Structure

```text
Task3-RAG-KnowledgeAnalyst/

├── app.py
├── pdf_processor.py
├── rag_engine.py
├── dashboard.py
├── prompts.py
├── requirements.txt
├── .env
├── README.md

├── source_documents/
├── outputs/
└── screenshots/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Knowledge-Analyst-RAG-System.git
```

Move into the project folder:

```bash
cd Knowledge-Analyst-RAG-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Running the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

## Screenshots

The screenshots folder contains:

- PDF Upload Interface
- Document Summary
- Risk Analysis Dashboard
- Date Extraction Results
- Stakeholder Analysis
- Question Answering Interface

## Learning Outcomes

Through this project, the following concepts were explored:

- Retrieval-Augmented Generation (RAG)
- Document Intelligence
- Prompt Engineering
- AI-Powered Summarization
- Vector Search Concepts
- Large Language Models (LLMs)
- Streamlit Application Development

## Future Improvements

- Real FAISS Vector Search Integration
- Embedding-Based Retrieval
- Multi-Document Support
- Citation-Based Responses
- Advanced Dashboard Analytics
- Cloud Deployment

## Author

Mohit Prajapati

Generative AI Intern

DecodeLabs Internship Program 2026
