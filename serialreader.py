# Program that reads data from an arduino connected to the device via a COM port
# By Samyak Doshi

# importing necessary modules
import serial
from serial.serialutil import SerialException

try:  

    file = open("D:\\Falcons\\Task 1\\log.csv", "w", newline="") #opening the file
    ser = serial.Serial('COM13', 9600) #opening a serial pipe at the specified COM port and baud rate

    while True:
        # Read and format data from serial port
        data1 = ser.readline().decode().strip()
        millis, dist = data1.split(',')

        # Print and write data to CSV file
        print(f"Seconds: {millis}, Distance: {dist}\n")
        file.write(f"Seconds: {millis}, Distance: {dist}\n")

except SerialException as e: #catching the device being disconnected 
    print("Device disconnected! \n")
    file.write("Device disconnected! \n")

except ValueError as e: #catching when half a packet of data is received, then device disconnects
    print("Device disconnected! \n")
    file.write("Device disconnected! \n")

except KeyboardInterrupt as e: #catching the human intended exit
    print("User intended break \n")
    file.write("User intended break \n")

finally:
    # Close the CSV file
    file.close()

