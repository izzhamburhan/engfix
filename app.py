import streamlit as st
# from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Functions to get responses from LLama 2 model
def getLLamaResponse(input_text, no_words, blog_style) :

    ### LLama 2 model functions
    llm=CTransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                      model_type='llama',
                      config={'max_new_tokens':256,
                             'temperature':0.01})
    
    ## Prompt Template
    template = """
                Buat blog untuk {blog_style} berkenaan topik {input_text}
                dalam {no_words} patah perkataan. (answer in Bahasa Malaysia)
                """
    
    prompt = PromptTemplate(input_variables=['blog_style','input_text','no_words'],
                            template=template)
    
    ## Generate the response from the LLama 2 model
    # llm_chain = LLMChain(prompt=prompt , llm=llm)
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))

    print(response)
    return response


st.set_page_config(page_title="Teknik Sains Data",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('Teknik Sains Data 🤖')

input_text = st.text_input("Masukkan keywords yang anda ingin tahu")

## Craeting two more columns for additional 2 fields
col1, col2 = st.columns([5,5])

with col1:
    no_words=st.text_input("Bil. Perkataan")

with col2:
    blog_style = st.selectbox('Tulisan ini untuk :', 
                              ('Pengkaji', 'Data Saintis', 'Orang Awam'), 
                              index=0)

submit = st.button('Jana')


## Final Response
if submit:
    st.write(getLLamaResponse(input_text, no_words, blog_style))