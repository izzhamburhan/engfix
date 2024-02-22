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
                text : ''' {input_text} '''  
                instruction : ''' {blog_style}'''
                no. of words : ''' {no_words} '''

                    
                if the instruction is 'fix' , fix the grammer in the text and response within {no_words} words
                else if the instruction is 'reply' , reply the text in professional english within {no_words}


                """
    
    prompt = PromptTemplate(input_variables=['blog_style','input_text','no_words'],
                            template=template)
    
    ## Generate the response from the LLama 2 model
    # llm_chain = LLMChain(prompt=prompt , llm=llm)
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))

    print(response)
    return response


st.set_page_config(page_title="EngFix",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('EngFix 🤖')

input_text = st.text_area("Enter your text...")

## Craeting two more columns for additional 2 fields
col1, col2 = st.columns([5,5])

with col1:
    no_words=st.text_input("No. of words")

with col2:
    blog_style = st.selectbox('Instruction :', 
                              ('Fix Grammar', 'Reply'), 
                              index=0)

submit = st.button('Generate')


st.text('Response :')
## Final Response
if submit:
    st.write(getLLamaResponse(input_text, no_words, blog_style))