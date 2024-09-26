""" Example use of Module - Written by Benjamin Jack Cullen """

import askollama_3


log_file = './ollama_messages_0.dat'

askollama_3.load_ollama_log(log_file=log_file)
print(askollama_3.ask_ollama(log_file=log_file, role='user', content='Why is the sky blue?'))
# we can continue now or program can even be terminated, we can pick up where we left off providing we load ollama log.
print(askollama_3.ask_ollama(log_file=log_file, role='user', content='What was the last question I asked?'))
