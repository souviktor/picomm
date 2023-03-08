import time

filename_tof1 = "tof1.txt"
filename_tof2 = "tof2.txt"
filename_ard1 = "ard1.txt"
filename_ard2 = "ard2.txt"

while True:
    # Read the contents of tof1.txt and print with timestamp
    with open(filename_tof1, "r") as file:
        contents_tof1 = file.read().strip()
        if contents_tof1:
            print(f"[{time.time()}] tof1: {contents_tof1}")
    
    # Read the contents of tof2.txt and print with timestamp
    with open(filename_tof2, "r") as file:
        contents_tof2 = file.read().strip()
        if contents_tof2:
            print(f"[{time.time()}] tof2: {contents_tof2}")
    
    # Read the contents of ard1.txt and print with timestamp
    with open(filename_ard1, "r") as file:
        contents_ard1 = file.read().strip()
        if contents_ard1:
            print(f"[{time.time()}] ard1: {contents_ard1}")
    
    # Read the contents of ard2.txt and print with timestamp
    with open(filename_ard2, "r") as file:
        contents_ard2 = file.read().strip()
        if contents_ard2:
            print(f"[{time.time()}] ard2: {contents_ard2}")

    # Wait for a short interval before checking again
    time.sleep(0.1)

