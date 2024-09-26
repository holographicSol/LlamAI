import os.path
import time
import subprocess
import re

""" AI Driven Module - Written by Benjamin Jack Cullen """

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0
matrix = []


def get_matrix(file_name: str) -> bool:
    """ intends to produce a literal matrix from a matrix represented as a string. should not require modification """
    global matrix
    if os.path.exists(file_name):
        matrix_str = ''
        with open(file_name, 'r') as fo:
            for line in fo:
                line = line.strip()
                if not line.startswith('#'):
                    matrix_str = matrix_str + line
        try:
            matrix = eval(f"[{matrix_str}]")
            [print(f"{key}: {value}") for key, value in matrix[0][0].items()]
            return True
        except TypeError as e:
            print(e)


def ollama():
    """ instruct OLLAMA to process data, instead of writing any specific algorithm. should not require modification """

    # 1: start ollama server with a model
    ai_server_process = subprocess.Popen(['ollama', 'run', 'llama3.1'],
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT)
    # 2: harvest some data from somewhere (from anywhere you like, internet, cli tools, external embedded devices, etc.)
    data = ""
    xcmd = subprocess.Popen(matrix[0][0].get('COMMAND'),
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    while True:
        output = xcmd.stdout.readline()
        if output == '' or xcmd.poll() is not None:
            break
        if output:
            output_decoded = output.decode("utf-8").strip()
            data = data + '\n' + output_decoded
    xcmd.poll()
    # 3: ask ollama a question about the data
    if data:
        while True:
            ai_server_process.stdout.flush()
            ai_server_process.stdin.write(str(matrix[0][0].get('QUERY') + ': ' + data).encode())
            ai_server_process.stdin.flush()
            ai_response, any_str = ai_server_process.communicate(timeout=60)
            if not ai_response:
                break
            else:
                ai_response = ai_response.decode("utf-8").strip()
                break
        # 4: sanitize the response by removing only non-ascii chars and removing spaces, return response
        cleaned_ai_response = re.sub(r'[^\x00-\x7F]', '', ai_response)
        cleaned_ai_response = cleaned_ai_response.strip()
        # cleaned_ai_response = cleaned_ai_response.replace(' ', '')
        return cleaned_ai_response
