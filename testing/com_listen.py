import os
import serial

matrix = []


def get_matrix(file_name: str):
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


def com_listen():
    try:
        arduino_connection = serial.Serial(matrix[0][0].get('COM'), matrix[0][0].get('BAUD_RATE'))
        print(f"Connected to {matrix[0][0].get('COM')} at {matrix[0][0].get('BAUD_RATE')} bps")

        for i in range(0, 10):
            incoming_data = arduino_connection.readline()
            if incoming_data:
                data = incoming_data.decode('utf-8').strip()
                print(data)

    except serial.SerialException as e:
        print(f"Error connecting to COM port: {e}")


if get_matrix('./com_port.dat') is True:
    com_listen()
