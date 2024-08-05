# Novel Text-Summarization-and-Translation

This project provides a simple web application for novel text summarization and translation using Streamlit and Hugging Face Transformers library. The app allows users to input a paragraphs of Novel, generate a concise summary in English, and then translate that summary into Urdu.

## Features

* **Text Summarization**: Generate a summary of the input text using the `Falconsai/text_summarization` model.
* **Translation to Urdu**: Translate the English summary into Urdu using the `Helsinki-NLP/opus-mt-en-ur` model.

## Installation
1. Install the requirements file:
``` 
  pip install -r requirements.txt
```
2. Install the required libraries:

```     
  pip install streamlit transformers
```
## Steps
### 1. Import Libraries

  Import necessary libraries including Streamlit and Transformers for building the app and handling NLP tasks.
  ```python
import streamlit as st
from transformers import pipeline
```
### 2. Initialize Pipelines

  Define functions to load summarization and translation models, using caching to improve performance.
  ```python
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="Falconsai/text_summarization")

@st.cache_resource
def load_translator():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-ur")
```
### 3. Summarize Text Function

  Create a function that takes input text and returns a summarized version using the loaded summarizer model.
  ```python
def summarize_text(input_text, summarizer):
    summary = summarizer(input_text, max_length=700, min_length=100, do_sample=False)
    return summary[0]['summary_text']
```

### 4. Translate to Urdu Function

  Develop a function that translates the English summary into Urdu using the loaded translator model.
  ```python
def translate_urdu(english_summary, translator):
    urdu_text = translator(english_summary)
    return urdu_text[0]['translation_text']
```
  
### 5. Streamlit App

  Design the main function to build the Streamlit app, including text input, buttons, and display areas for summaries and translations.
## Use Cases

- **Content Creation**:
  
     Quickly generate summaries of long articles or documents and translate them into different languages.
- **Learning and Education**:
  
     Summarize educational material for easier understanding and translate it for non-English speakers.
## [Hugging Face Space URL](https://huggingface.co/spaces/ahmadmac/Text_summarization_translation)


