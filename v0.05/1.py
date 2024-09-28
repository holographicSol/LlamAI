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
    data = comparse.com_listen(com_num='COM8', baud_rate=115200)
    data = data.split(',')
    # add coordinates: done
    # add date
    # add time
    # add precision and number of satellites, inertial navigation system data.
    # parse other embedded systems output in the same way or add more sensors to SATCOM.
    return str(data[3] + str(', ') + data[4])


def main():
    # load data
    data = get_data()
    # ask a question about the data
    user_input = input(": ")
    t0 = time.time()
    r = askllama.ask_ollama(log_file=log_file,
                            log=True,
                            role='user',
                            content=user_input + '. My coordinates are: ' + data)
    print(r)
    print(time.time() - t0)

    """ do something, anything! on the local system, remote system(s), or send a message back over a COM port to control
       an embedded system """


if __name__ == '__main__':
    # retrieve message memory
    askllama.load_ollama_log(log_file=log_file)
    # loop main
    while True:
        try:
            main()
        except KeyboardInterrupt:
            exit(0)
