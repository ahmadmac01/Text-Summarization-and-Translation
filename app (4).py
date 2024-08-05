import streamlit as st
from transformers import pipeline

# Function to initialize pipelines with caching
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="Falconsai/text_summarization")

@st.cache_resource
def load_translator():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-ur")

def summarize_text(input_text, summarizer):
    summary = summarizer(input_text, max_length=700, min_length=100, do_sample=False)
    return summary[0]['summary_text']

def translate_urdu(english_summary, translator):
    urdu_text = translator(english_summary)
    return urdu_text[0]['translation_text']

def main():
    st.title("Text Summarization and Translation")
    input_text = st.text_area("Enter text to summarize:", "")

    if 'english_summary' not in st.session_state:
        st.session_state.english_summary = ""

    if 'urdu_translation' not in st.session_state:
        st.session_state.urdu_translation = ""

    summarizer = load_summarizer()
    translator = load_translator()

    if st.button("Summarize"):
        if input_text:
            english_summary = summarize_text(input_text, summarizer)
            st.session_state.english_summary = english_summary
            st.header("English Summary:",divider='gray')
            st.write(english_summary)

    if st.session_state.english_summary:
        if st.button("Translate English to Urdu"):
            urdu_translation = translate_urdu(st.session_state.english_summary, translator)
            st.session_state.urdu_translation = urdu_translation
            st.write("Urdu Translation:")
            st.write(urdu_translation)
            st.header("English Summary Text:",divider='gray')
            st.write(st.session_state.english_summary)

if __name__ == "__main__":
    main()


