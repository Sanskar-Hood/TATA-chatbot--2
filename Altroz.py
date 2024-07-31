import streamlit as st
from altroz_main import altroz_bot_query

# Function to simulate LLM response for Nexon
def get_llm_response_altroz(question):
    ans = altroz_bot_query(question+"altroz")
    return f"Answer to: {ans}"

# Initialize session state for conversation history specific to Nexon
if 'altroz_conversation' not in st.session_state:
    st.session_state.altroz_conversation = []

# Title of the app
st.title("Altroz")

# Display the conversation history for Nexon
if st.session_state.altroz_conversation:
    for i, (question, answer) in enumerate(st.session_state.altroz_conversation):
        st.write(f"**Q{i+1}:** {question}")
        st.write(f"**A{i+1}:** {answer}")

# Form for user input specific to Nexon
with st.form(key='altroz_input_form', clear_on_submit=True):
    user_input = st.text_input("Ask a question about Altroz:")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if user_input:
            response = get_llm_response_altroz(user_input)
            st.write(response)
            # Store the question and response in session state specific to Nexon
            st.session_state.altroz_conversation.append((user_input, response))
