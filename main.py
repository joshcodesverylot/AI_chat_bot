from ollama import chat
from config import model
import json

messages = []

with open('chat_history.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

print("Ollama chat, Please type exit to quit")

response = chat(model=model, messages=messages)

while True:


    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Have a nice day")
        break

    
    messages.append({"role": "user", "content": user_input})

    response = chat(model=model, messages=messages)

    assistant_reply = response['message']['content']
    print(f"AI: {assistant_reply}")


    messages.append({"role": "assistant", "content": assistant_reply})

with open("chat_history.json", "w") as f:
    json.dump(messages, f, indent=4)