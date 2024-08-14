import serial
from psychopy import core

port_name = 'COM3'
globalClock = (core.Clock())


def serial_marker():
    ser = serial.Serial(port_name)
    ser.write(str.encode('1'))
    stimulus_pulse_start_time = globalClock.getTime()
    running = True
    while running:
        if globalClock.getTime() - stimulus_pulse_start_time >= 0.05:
            ser.write(str.encode('0'))
            running = False
if __name__ == '__main__':
    serial_marker()