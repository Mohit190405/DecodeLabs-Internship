import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("AIzaSyB0KtA9hOQ6pLJJmDRORnAocc0_LicTcQ0")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

st.set_page_config(
    page_title="Multimodal Content Engine"
)

st.title("🎥 Multimodal Content Engine")

st.write(
    "Paste video transcript below."
)

transcript = st.text_area(
    "Video Transcript",
    height=300
)

if st.button("Generate Content"):

    prompt = f"""
    Analyze this transcript.

    Generate:

    1. Summary
    2. Top 5 Viral Moments
    3. Instagram Caption
    4. YouTube Shorts Caption
    5. Viral Headlines
    6. B-Roll Suggestions

    Transcript:

    {transcript}
    """

    response = model.generate_content(prompt)

    st.subheader("Generated Output")

    st.write(response.text)

    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/final_output.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(response.text)

    st.success(
        "Output saved successfully."
    )