import paho.mqtt.client as mqtt

# Define the IP address of the MQTT broker
broker_address = "192.168.0.228"

# Define the filename for writing the received messages
filename_tof1 = "tof1.txt"
filename_tof2 = "tof2.txt"

# Define the callback function for handling messages
def on_message(client, userdata, message):
    # Decode the message payload and write it to the file
    message_str = str(message.payload.decode("utf-8"))
    if message.topic == "tof1":
        with open(filename_tof1, "w") as file:
            file.write(message_str + "\n")
        print("Received message for tof1: ", message_str)
    elif message.topic == "tof2":
        with open(filename_tof2, "w") as file:
            file.write(message_str + "\n")
        print("Received message for tof2: ", message_str)

# Create an MQTT client instance and set the callback function
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker and subscribe to the topics
client.connect(broker_address)
client.subscribe("tof1")
client.subscribe("tof2")

# Loop forever and handle incoming messages
client.loop_forever()

