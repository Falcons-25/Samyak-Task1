# Arduino Sensor Data Logger

This project demonstrates how to use an Arduino board to read sensor data and send it to a computer via the serial port. The computer then reads the serial port data using a Python script, which automatically detects the serial port and stores the data in a CSV file.

## Components Used
- Arduino board (e.g., Arduino Uno)
- Ultrasonic sensor (or any other sensor of your choice)
- USB cable for connecting the Arduino to your computer
- Computer with Python installed

## Arduino Setup
1. **Connect the Sensor:**
   - Connect your sensor to the Arduino board. For an ultrasonic sensor, connect the VCC to 5V, GND to GND, Trigger pin to a digital pin (e.g., D9), and Echo pin to another digital pin (e.g., D10).

2. **Upload the Arduino Code:**
   - Use the Arduino IDE to upload the code [(here)](ultrasonic_out.ino) to your Arduino board. 
   - Remember the serial baud rate and the COM port of your arduino.


## Python Script
1. **Install Required Libraries:**
   - Ensure you have `pyserial` installed. You can install it using pip:
     ```sh
     pip install pyserial
     ```

2. **Python Code:**
   - Create a Python script (e.g., `serialreader.py`) with the reference code [(here)](serialreader.py) to read the serial data and save it to a CSV file.
   - Change the COM port and the baud rate as per your system and configurations.


## How to Run
1. **Upload the Arduino Code:**
   - Connect your Arduino to your computer and upload the Arduino code using the Arduino IDE.

2. **Run the Python Script:**
   - Ensure your Arduino is connected via USB.
   - Run the Python script:
     ```sh
     python serialreader.py
     ```

3. **Check the Output:**
   - The Python script will automatically detect the Arduino serial port, read the distance data, display it in the output and append it to `"D:\Falcons\Task 1\log.csv"`. Each entry will include the distance measurement.
