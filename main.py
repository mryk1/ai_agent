import streamlit as st
import json
import os
from agent import ask_agent

st.set_page_config(page_title="AI Agent Chat", layout="centered")

st.title("AI Agent Chat")
st.write("Ask me anything!")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if user_input:
    answer, updated_history = ask_agent(user_input, st.session_state.history)
    st.session_state.history = updated_history

    for user, ai in st.session_state.history:
        st.write(f"**You:** {user}")
        st.write(f"**Agent:** {ai}")

    # Save chat to file
    with open("chat_history.json", "w") as f:
        json.dump(st.session_state.history, f, indent=2)