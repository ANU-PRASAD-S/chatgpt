import os
import openai
import streamlit as st
from typing import List
from dotenv import load_dotenv

openai.api_key = os.getenv("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")
st.set_page_config(page_title="Chat Interface", page_icon=":robot_face:", layout="wide")

openai.api_key = os.getenv("OPENAI_API_KEY")
st.set_page_config(page_title="Chat Interface", page_icon=":robot_face:", layout="wide")

def generate_response(messages: List[dict]) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

chat_container = st.container()
user_input = st.text_input("You: ", "Type your message here...")


submit_button = st.button("Send")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

if submit_button and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = generate_response(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "assistant":
            st.markdown(f'**Assistant:** {message["content"]}', unsafe_allow_html=True)
        else:
            st.markdown(f'**You:** {message["content"]}', unsafe_allow_html=True)

st.title("Chat Interface")
st.write("Ask me anything!")
st.run_script("chat_interface.py")


