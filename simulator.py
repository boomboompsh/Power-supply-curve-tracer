# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:23:16 2020
 simulates the behavior of the MOSFET circuit used in the power 
 supply curve tracer project, controls it, and displays results.
@author: Andrew Stone
"""


import serial
import matplotlib.pyplot as plt
import keyboard
simmatrix = []
with open("currentsvoltagesfixed.csv","r") as file:
    file.readline()
    for line in file:
        simmatrix.append(line.split(";"))

with serial.Serial('COM3', 9600) as ser:
    ser.write(b'B')
    mode = 'S'
    voltages = []
    currents = []
    while(1):
        inputduty = int(ser.readline())
        
        vdat = simmatrix[inputduty][1]
        cdat = simmatrix[inputduty][2]
        ser.write(bytes("F "+vdat+" "+cdat,"utf-8"))
        if mode == 'G':
            voltages.append(float(ser.readline()))
            currents.append(float(ser.readline()))
        char = ''
        
        char = keyboard.read_key()
        if mode == "S":
            print("Voltage:",float(ser.readline()),"Current:",float(ser.readline()))
        if char == "s":
            setpoint = input("Enter the desired current in amps: ")
            ser.write(bytes("S "+setpoint,"utf-8"))
        elif char == "g":
            print("Entering Graph Mode")
            mode = "G"
            ser.write(b'G')
        if inputduty == 0 and mode == 'G':
            mode ='S'
            plt.plot(voltages, currents);
            plt.xlabel("Voltage (V)")
            plt.ylabel("Current (A)")
        if char == 'q':
            print("Goodbye!")
            break
        


            
            
            
            
            