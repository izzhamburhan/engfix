import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Functions to get responses from LLama 2 model







st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.head('Generate Blogs 🤖')

input_text = st.text_input("Enter the Blog Topic")

## Craeting two more columns for additional 2 fields
col1, col2 = st.columns([5,5])

with col1:
    no_words=st.text_input("No. of Words")

with col2:
    blog_style = st.selectbox('Writing the Blog Style')