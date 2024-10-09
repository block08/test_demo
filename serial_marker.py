import serial
from psychopy import core

port_name = 'COM3'
globalClock = (core.Clock())


def serial_marker(data_to_send):
    ser = serial.Serial(
        port=port_name,  # 修改为你的串口名，例如 'COM3' (Windows) 或 '/dev/ttyUSB0' (Linux)
        baudrate=57600,  # 波特率
        bytesize=serial.EIGHTBITS,  # 8个数据位
        parity=serial.PARITY_NONE,  # 无奇偶校验
        stopbits=serial.STOPBITS_ONE,  # 1个停止位
        timeout=1  # 可选的超时设置
    )
    clear_zero = bytes([0b00000000])
    ser.write(data_to_send)
    stimulus_pulse_start_time = globalClock.getTime()
    running = True
    while running:
        if globalClock.getTime() - stimulus_pulse_start_time >= 0.05:
            ser.write(clear_zero)
            running = False
