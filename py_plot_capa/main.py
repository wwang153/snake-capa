# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)

data = []
for i in range(50):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        mid_data = string.replace("\r\n", "")
        print(mid_data)

ser.close()

# plt.plot(data)
#
# plt.show()