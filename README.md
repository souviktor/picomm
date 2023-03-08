# picomm

This repo contains files to facilitate communication between different pis and arduinos to one central pi. 

The pi-pi comm is based on mqtt, taken from here:https://mohamedelhlafi.medium.com/use-the-mqtt-protocol-to-communicate-data-between-2-raspberry-pi-3d432dea9313

The arduino-pi is simple serial UART: https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/

Codes: 
1. Listener.py listens to a local broker running on the main py. Apperently the broker is always on by default. If not, restart the service. 
2. ard1.py, ard2.py reads from various connected arduinos (2 here). To get their device address, check use: 
  ls /dev/tty* and see if there are ttyACM0 and ttyUSB0 devices ( the 2 aruduinos connected to the 2 usb ports)
3. master.py is going to teh sensor fusion algo which reads from tof1.txt, tof2.txt, ard1.txt and ard2.txt and prints in on console. 


In addition, on each of the 2 pis, we will need a python script to send data, that code is mqtt_test.py

  
Steps: 
1. First install mqtt on all pis:
-> sudo apt-get install -y mosquitto mosquitto-clients
2. The previous command will have automatically strated the broker. but if you run into any issues, restrat : 
->sudo systemctl restart mosquitto
3. The listener.py and ard1.py and ard2.py are all listening for incoming data and saving into files. run them one by one, each from a different terminal
-> python listener.py
-> python3 ard1.py
-> python3 ard2.py

4. At this point the main pi will be listening from 2 pis and 2 arduinos. If you have additional devices, you need additional arduino/pico you can create ard3.py etc. 
If you have additional pi devices, just modify the listener.py to listen a new channel. 

5. on the client pis, you can run the mqtt_test.py to produce data continuously to test if the communication is working. You need to use the code in mqtt_test.py in your actual data acquisition loop to enable sending actual data. 

6. On teh main py, you can run master.py to just quickly check if all files are being updated in real time. 


