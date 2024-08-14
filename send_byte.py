import serial
import time

# 打开串口
ser = serial.Serial('COM3', 9600, timeout=0.5)  # 确保串口名称和波特率正确

# 发送数据
data_to_send = b'\x01'  # 字节数据
ser.write(data_to_send)

# 接收数据
time.sleep(0.1)  # 等待接收缓冲区清空，根据实际情况调整时间
received_data = ser.read(len(data_to_send))

# 输出接收到的数据
print(received_data)

# 关闭串口
ser.close()