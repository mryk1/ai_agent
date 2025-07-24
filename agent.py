import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_agent(question, history=None):
    if history is None:
        history = []

    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    for user, ai in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": ai})
    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = response["choices"][0]["message"]["content"]
    history.append((question, answer))
    return answer, history
