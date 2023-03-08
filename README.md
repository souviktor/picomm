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

  
