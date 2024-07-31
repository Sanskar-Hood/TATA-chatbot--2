import streamlit as st
from Tiago_main import tiago_bot_query

# Function to simulate LLM response for Tiago
def get_llm_response_tiago(question):
    ans = tiago_bot_query(question+"tiago")
    return f"Answer to: {ans}"

# Initialize session state for conversation history specific to Tiago
if 'tiago_conversation' not in st.session_state:
    st.session_state.tiago_conversation = []

# Title of the app
st.title("Tiago")

# Display the conversation history for Tiago
if st.session_state.tiago_conversation:
    for i, (question, answer) in enumerate(st.session_state.tiago_conversation):
        st.write(f"**Q{i+1}:** {question}")
        st.write(f"**A{i+1}:** {answer}")

# Form for user input specific to Tiago
with st.form(key='tiago_input_form', clear_on_submit=True):
    user_input = st.text_input("Ask a question about Tiago:")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if user_input:
            response = get_llm_response_tiago(user_input)
            st.write(response)
            # Store the question and response in session state specific to Tiago
            st.session_state.tiago_conversation.append((user_input, response))
