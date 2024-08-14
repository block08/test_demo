import serial


def check_serial_connection(serial_name):
    try:
        ser = serial.Serial(serial_name)
        return True
    except serial.SerialException as e:
        print(f"Error opening serial port {serial_name}: {str(e)}")
        return False