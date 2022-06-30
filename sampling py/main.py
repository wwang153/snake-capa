import serial
from pynput import keyboard
from pynput.keyboard import Key, Listener, KeyCode
import csv
import threading
import time

# global variables
flag = False  # for keyboard input
line_1 = 0  # value read from snake
line_2 = 0  # value read from encoder

# initialize the serial communication
ser1 = serial.Serial("COM5", 9600, timeout=0.3)  # snake COM port
ser2 = serial.Serial("COM12", 9600, timeout=0.1)  # calibration tool COM port


def press_callback(key):  # trigger for starting sampling from 2 COM port
    global flag
    global line_1, line_2

    if key == KeyCode.from_char('c'):
        flag = True
        print("(C) is pressed, start sampling.")
    elif key == KeyCode.from_char('s'):
        flag = False
        print('(S) Sample stop due to user input')

    if flag:
        for i in range(50):
            time.sleep(0.3)  # sampling rate change here
            print(line_1)
            str1 = line_1.decode()
            data1 = str1.replace("\r\n", "").split(', ')
            with open('C:/Users/transferRNA/Desktop/snake capa/data/test_csv.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(data1)

        # for i in range(105):
        #     line1 = ser1.readline()
        #     line2 = ser2.readline()
        #     if line1:
        #         # str2 = line2.decode()
        #         # data2_temp = str2.replace("\r\n", "").split(', ')
        #         # data2_temp1 = list(map(float, data2_temp))
        #         # print(data2_temp1)
        #         if i > 5:
        #             str1 = line1.decode()
        #             data1 = str1.replace("\r\n", "").split(', ')
        #             with open('C:/Users/transferRNA/Desktop/snake capa/Collected Data/test_csv.csv', 'a',
        #                       newline='') as file:
        #                 writer = csv.writer(file, delimiter=',')
        #                 writer.writerow(data1)


def release_callback(key):  # command for stopping sampling
    if key == keyboard.Key.esc:
        print("Stop sampling program.")
        return False


def read_calibrate():
    x = threading.Thread(target=thread_function)  # include the reading value thread
    x.start()
    # enable the keyboard listener
    l = keyboard.Listener(on_press=press_callback, on_release=release_callback)
    l.start()
    l.join()


def thread_function():  # value reading thread
    global line_1, line_2
    while 1:
        # time.sleep(0.1)
        line_1 = ser1.readline()
        line_2 = ser2.readline()


if __name__ == '__main__':
    read_calibrate()
