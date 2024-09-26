""" Application Template - Written by Benjamin Jack Cullen """

import subprocess
import time
import askllama
import comparse

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0
matrix = []
log_file = './ollama_messages_0.dat'


def get_data():
    """ this template obtains data from an embedded system (SATCOM available in my repos) and isolates lat/long.
    another example may instead be like "are coordinates x closer to coordinates y than previous coordinates" '
    """
    data = comparse.com_listen(com_num='COM5', baud_rate=115200)
    data = data.split(',')
    return str(data[3] + str(', ') + data[4])


def main():
    # load data
    data = get_data()
    # ask a question about the data
    r = askllama.ask_ollama(log_file=log_file,
                            log=True,
                            role='user',
                            content='Answer by responding in two words: City and Country.'
                                    'Geolocate these coordinates: ' + str(data))
    print(r)

    """ do something, anything! on the local system, remote system(s), or send a message back over a COM port to control
       an embedded system """


if __name__ == '__main__':
    # retrieve message memory
    askllama.load_ollama_log(log_file=log_file)
    # loop main
    while True:
        try:
            main()
            time.sleep(3)
        except KeyboardInterrupt:
            exit(0)
