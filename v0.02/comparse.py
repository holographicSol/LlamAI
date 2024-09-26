""" Written by Benjamin Jack Cullen """

import serial


def com_listen(com_num: str, baud_rate: int) -> str:
    """ connects to a COM port and returns results """
    try:
        data = ''
        arduino_connection = serial.Serial(com_num, baud_rate)
        for i in range(0, 10):
            incoming_data = arduino_connection.readline()
            if incoming_data:
                tmp_data = incoming_data.decode('utf-8').strip()
                data = data + tmp_data
        return data
    except serial.SerialException as e:
        print(f"Error connecting to COM port: {e}")
