""" Application Template - Written by Benjamin Jack Cullen """

import subprocess
import time
import askllama

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0
matrix = []
log_file = './ollama_messages_0.dat'


def get_data():
    """ get data from somewhere (from anywhere you like, internet, cli, external embedded devices, etc.) """
    data = ""
    xcmd = subprocess.Popen('ping -n 1 8.8.8.8',
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
    return data


def main():
    # retrieve message memory
    askllama.load_ollama_log(log_file=log_file)
    # load data
    data = get_data()
    # ask a question about the data instead of the traditional way of creating infinite never ending  custom algorithms
    r = askllama.ask_ollama(log_file=log_file,
                             role='user',
                             content='Answer by responding exactly with either True of False (like pythonic bool).'
                                     'According to the ping, am I online?: ' + str(data))
    print(r)

    # do something, anything! on the local system, remote system(s), or send a message back over a COM port to control an embedded system


if __name__ == '__main__':
    while True:
        try:
            main()
            time.sleep(3)
        except KeyboardInterrupt:
            exit(0)
