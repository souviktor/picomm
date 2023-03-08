import serial

# Define the filename for writing the received messages
filename_ard1 = "ard1.txt"

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            # Read the message from the serial port
            line = ser.readline().decode('utf-8').rstrip()
            
            
            # Write the message to ard1.txt
            with open(filename_ard1, "w") as file:
                file.write(line + "\n")
            print("Received message for ard1: ", line)

