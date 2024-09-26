""" A conversation with Llama (with logging) - Written by Benjamin Jack Cullen """

import os.path

import ollama


client = ollama.Client()
messages = []
log_file = './ollama_messages_0.dat'


def ollama_log(message: list):
    """ write messages to file """
    with open(log_file, 'a+') as fo:
        fo.write(str(message)+',\n')
    fo.close()


def load_ollama_log():
    """ read ollama messages history from file """
    global messages
    if os.path.exists(log_file):
        matrix_str = ''
        with open(log_file, 'r') as fo:
            for line in fo:
                line = line.strip()
                if not line.startswith('#'):
                    matrix_str = matrix_str + line
        print(matrix_str)
        if matrix_str:
            try:
                messages = eval(f"[{matrix_str}]")
                print(messages)
                [print(f"{key}: {value}") for key, value in messages[0].items()]
                return True
            except TypeError as e:
                print(e)


def ask_ollama(role: str, content: str):
    messages.append(
        {
            'role': role,
            'content': content,
        }
    )
    ollama_log(message=messages[-1])
    response = client.chat('llama3.1', messages=messages)
    messages.append(response['message'])
    ollama_log(message=messages[-1])
    print(response['message']['content'])


load_ollama_log()
ask_ollama(role='user', content='Why is the sky blue?')
# we can continue now or program can even be terminated, we can pick up where we left off providing we load ollama log.
ask_ollama(role='user', content='What was the last question I asked?')
