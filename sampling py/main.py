import serial
from pynput import keyboard
from pynput.keyboard import Key, Listener, KeyCode
import csv

# global variables
flag = False

# initialize the serial communication
ser1 = serial.Serial("COM5", 9600, timeout=0.1)  # snake COM port
ser2 = serial.Serial("COM12", 9600, timeout=0.1)  # calibration tool COM port


def press_callback(key):  # trigger for starting sampling from 2 COM port
    global flag
    if key == KeyCode.from_char('c'):
        flag = True
        print("(C) is pressed, start sampling.")
    elif key == KeyCode.from_char('s'):
        flag = False
        print('Sample stop due to user input')

    if (flag == True):
        for i in range(50):
            line1 = ser1.readline()
            line2 = ser2.readline()
            if line1:
                print(line1)
                print(i)
                i = i + 1


def release_callback(key):  # command for stopping sampling
    global flag
    if key == keyboard.Key.esc:
        flag = False
        print("Stop sampling program.")
        return False


def read_calibrate():  # enable the keyboard listener
    global i
    l = keyboard.Listener(on_press=press_callback, on_release=release_callback)
    l.start()
    l.join()


if __name__ == '__main__':
    read_calibrate()