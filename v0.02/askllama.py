""" A module for conversation with Llama (with logging) - Written by Benjamin Jack Cullen """

import os.path
import ollama


client = ollama.Client()
messages = []


def ollama_log(log_file: str, message: list):
    """ write messages to file """
    with open(log_file, 'a+') as fo:
        fo.write(str(message)+',\n')
    fo.close()


def load_ollama_log(log_file: str):
    """ read ollama messages history from file """
    global messages
    if os.path.exists(log_file):
        matrix_str = ''
        with open(log_file, 'r') as fo:
            for line in fo:
                line = line.strip()
                if not line.startswith('#'):
                    matrix_str = matrix_str + line
        fo.close()
        if matrix_str:
            messages = eval(f"[{matrix_str}]")


def ask_ollama(log_file: str, log: bool, role: str, content: str) -> str:
    """ queries llama and logs new message and response """
    messages.append(
        {
            'role': role,
            'content': content,
        }
    )
    if log is True:
        ollama_log(log_file=log_file, message=messages[-1])
    response = client.chat('llama3.1', messages=messages)
    messages.append(response['message'])
    if log is True:
        ollama_log(log_file=log_file, message=messages[-1])
    return response['message']['content']
