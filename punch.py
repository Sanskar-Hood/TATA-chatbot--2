import streamlit as st
from punch_main import punch_bot_query

# Function to simulate LLM response for Punch
def get_llm_response_punch(question):
    ans = punch_bot_query(question+"punch")
    return f"Answer to: {ans}"

# Initialize session state for conversation history specific to Punch
if 'punch_conversation' not in st.session_state:
    st.session_state.punch_conversation = []

# Title of the app
st.title("Punch")

# Display the conversation history for Punch
if st.session_state.punch_conversation:
    for i, (question, answer) in enumerate(st.session_state.punch_conversation):
        st.write(f"**Q{i+1}:** {question}")
        st.write(f"**A{i+1}:** {answer}")

# Form for user input specific to Punch
with st.form(key='punch_input_form', clear_on_submit=True):
    user_input = st.text_input("Ask a question about Punch:")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if user_input:
            response = get_llm_response_punch(user_input)
            st.write(response)
            # Store the question and response in session state specific to Punch
            st.session_state.punch_conversation.append((user_input, response))
