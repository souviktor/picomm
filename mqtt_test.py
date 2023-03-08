import time
import paho.mqtt.client as mqtt

# Define the IP address of the MQTT broker
broker_address = "192.168.0.228"
#change this accordiingly

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address)

# Set the topic
topic = "tof1"

# Loop and publish the message every 1 second
sequence_number = 0
while True:
    # Construct the message string with the sequence number
    message = f"Hello Raspberry Pi {sequence_number}"
    
    # Publish the message to the MQTT broker
    client.publish(topic, message)
    
    # Increase the sequence number for the next message
    sequence_number += 1
    
    # Wait for 1 second before publishing the next message
    time.sleep(0.05)
