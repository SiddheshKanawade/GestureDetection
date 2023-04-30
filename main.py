# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import serial
import numpy as np

from model import MLPModel
from data_processing import get_data

ser = serial.Serial('COM12', 9600)  # open serial port with baud rate 9600
filename = 'data.txt'  # name of file to save data to
file = open(filename, 'a')  # open file for writing

X, y = get_data()
# variable = 'ThankYou'
model = MLPModel()
model.train(X, y)

count = 0
while True:
    print("Reading Current Data...")
    data = ser.readline()  # read line of data from serial port
    data = data.decode('utf-8')  # convert bytes to string
    data = data.split('\n')
    data = data[0]
    data = data.split(',')
    data_x = []
    for item in data:
        item = int(item)
        data_x.append(item)
    # data = f"{data},{variable} \n"
    # data = data.split(',')
    # data = np.array(data_x)
    X = []
    X.append(data_x)
    print(f"Predicting data...{count}")
    predictions = model.predict(X)
    print(predictions)
    count = count+1


    # file.write(data)  # write data to file
    # file.flush()
    # print(data.strip())  # print data to console

file.close()
