import streamlit as st

from src.chat.chat_service import get_ai_response

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
)

st.title("🤖 AI Assistant")

username = st.text_input("Username", value="guest")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("Thinking..."):

        answer = get_ai_response(username, prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)