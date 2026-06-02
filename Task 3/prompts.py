SUMMARY_PROMPT = """
Summarize the following document.

Focus on:
1. Key points
2. Risks
3. Important dates
4. Stakeholders

Document:
{context}
"""

QA_PROMPT = """
Answer the question using only the provided context.

Context:
{context}

Question:
{question}
"""