import streamlit as st
from harrier_main import harrier_bot_query

# Function to simulate LLM response for Harrier
def get_llm_response_harrier(question):
    ans = harrier_bot_query(question+"harrier")
    return f"Answer to: {ans}"

# Initialize session state for conversation history specific to Harrier
if 'harrier_conversation' not in st.session_state:
    st.session_state.harrier_conversation = []

# Title of the app
st.title("Harrier")

# Display the conversation history for Harrier
if st.session_state.harrier_conversation:
    for i, (question, answer) in enumerate(st.session_state.harrier_conversation):
        st.write(f"**Q{i+1}:** {question}")
        st.write(f"**A{i+1}:** {answer}")

# Form for user input specific to Harrier
with st.form(key='harrier_input_form', clear_on_submit=True):
    user_input = st.text_input("Ask a question about harrier:")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if user_input:
            response = get_llm_response_harrier(user_input)
            st.write(response)
            # Store the question and response in session state specific to Harrier
            st.session_state.harrier_conversation.append((user_input, response))
