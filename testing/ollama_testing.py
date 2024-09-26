""" A conversation with Llama - Written by Benjamin Jack Cullen """

import ollama


client = ollama.Client()
messages = []


def ask_ollama(role: str, content: str):
    messages.append(
        {
            'role': role,
            'content': content,
        }
    )
    response = client.chat('llama3.1', messages=messages)
    messages.append(response['message'])
    print(response['message']['content'])


ask_ollama(role='user', content='Why is the sky blue?')
ask_ollama(role='user', content='What was the last question I asked?')
ask_ollama(role='user', content='Summarize the answer you gave?')
