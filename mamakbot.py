import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Functions to get responses from LLama 2 model
def getLLamaResponse(prompt):
    llm = CTransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    response = llm(prompt)
    return response

st.set_page_config(page_title="MamakBot",
                   page_icon='🍛',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('🍛 MamakBot')

# Define the initial context with the system message
context = [
    {
        'role': 'system',
        'content': """
        You are MamakBot, an automated service at a mamak restaurant.
        You speak informally like a mamak in Malay.
        You warmly greet customers, take their orders, provide options,
        and ask if they want any add-ons.
        After confirming the order, you inquire if they will be dining in
        or taking away. You wait for the complete order, summarize it, and
        double-check if they need anything else.
        If they are dining in, you ask for a table preference.
        Finally, you collect the payment.
        Make sure to explain menu items, choices, and sizes clearly to avoid any confusion.
        The menu includes:
        nasi lemak 6.95
        roti canai 1.50
        teh tarik 2.00
        maggi goreng 5.00
        roti telur 2.50
        roti bakar 1.75
        Toppings:
        telur mata 0.50
        sambal 0.75
        daging 2.50
        ayam 2.00
        Drinks:
        teh o ais 2.80
        limau ais 2.00
        air bandung 2.75
        milo ais 3.00
        """
    }
]

# Define a function to process the conversation
# Define a function to process the conversation
def process_conversation(user_input):
    # Append the user's message to the context
    context.append({'role':'user', 'content': user_input})
    # Concatenate the messages in the context list into a single prompt string
    prompt = "\n".join([message['content'] for message in context])
    # Generate response using LLama 2
    response = getLLamaResponse(prompt)
    # Append the assistant's response to the context
    context.append({'role':'assistant', 'content': response})
    
    return response

# Display the conversation history and input area
conversation = st.empty()
user_input = st.text_input("You:", "")

# Process user input and display responses
if st.button("Send"):
    response = process_conversation(user_input)
    conversation.write(f"Assistant: {response}")