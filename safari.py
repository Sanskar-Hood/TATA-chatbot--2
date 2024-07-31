import streamlit as st
from safari_main import safari_bot_query

# Function to simulate LLM response
def get_llm_response(question):
    ans = safari_bot_query(question)
    return f"Answer to: {ans}"

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Title of the app
st.title("SUVs")

# Display the conversation history
if st.session_state.conversation:
    for i, (question, answer) in enumerate(st.session_state.conversation):
        st.write(f"**Q{i+1}:** {question}")
        st.write(f"**A{i+1}:** {answer}")

# Form for user input
with st.form(key='input_form', clear_on_submit=True):
    user_input = st.text_input("Ask a question about SUVs:")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if user_input:
            response = get_llm_response(user_input)
            st.write(response)
            # Store the question and response in session state
            st.session_state.conversation.append((user_input, response))
            # Clear the input box after submitting
            # st.text_input("Ask a question about SUVs:", value="", key="new_input")
