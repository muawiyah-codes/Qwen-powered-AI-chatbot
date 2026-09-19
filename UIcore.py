from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Model
model = ChatGroq(
    model="qwen/qwen3.8-27b"
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ('system', """
    You are an intelligent information extraction assistant.

    Your job is to extract the most useful and relevant information from the
    text provided by the user.

    For movie-related text, identify information such as:
    - Movie Name
    - Release Year
    - Genre
    - Director
    - Main Cast
    - Music Composer
    - Main Plot
    - Key Themes
    - Important Locations or Setting
    - Rating
    - Rating Source
    - Notable Features
    - Audience or Critical Reception
    - Any other important information

    Also generate a short and clear summary of the provided text.

    Rules:
    - Extract information only from the provided text.
    - Do not assume or invent information.
    - If a detail is not mentioned, write "Not mentioned".
    - Keep the extracted information concise and well organized.
    - Correct minor spelling mistakes when necessary.
    - The summary should be 2-3 sentences.
    - Use clear headings for the extracted information.
    """),

    ('human', """
    Extract information from this paragraph:

    {paragraph}
    """)
])


# ---------------- STREAMLIT UI ----------------

st.set_page_config(
    page_title="CineSage",
    page_icon="🎬"
)

st.title("🎬 CineSage")
st.write("Extract useful information from a movie paragraph.")

para = st.text_area(
    "Enter a paragraph about a movie:",
    height=250,
    placeholder="Paste your movie paragraph here..."
)

if st.button("Extract Information"):

    if para.strip():

        final_prompt = prompt.invoke({
            "paragraph": para
        })

        response = model.invoke(final_prompt)

        st.subheader("Extracted Information")

        st.markdown(response.content)

    else:
        st.warning("Please enter a movie paragraph.")