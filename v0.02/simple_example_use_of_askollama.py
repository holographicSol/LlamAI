""" Example use of Module - Written by Benjamin Jack Cullen """

import askllama


log_file = './ollama_messages_0.dat'

askllama.load_ollama_log(log_file=log_file)
print(askllama.ask_ollama(log_file=log_file, role='user', content='Why is the sky blue?'))
# we can continue now or program can even be terminated, we can pick up where we left off providing we load ollama log.
print(askllama.ask_ollama(log_file=log_file, role='user', content='What was the last question I asked?'))
