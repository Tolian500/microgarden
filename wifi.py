import network
import time
import ubinascii
import requests
from machine import Pin
import random



def led(command:str, delay:float=1):
    pin = Pin("LED", Pin.OUT)
    if command is "on": 
        pin.toggle()
    if command is "off":
        pin.off()
    if command is 'blick':
        pin.toggle()
        time.sleep(delay/2)
        pin.off()
        time.sleep(delay/2)



def send_data(tablename:str, temp:float, hum:float):
    url = 'http://37.27.94.203:5000/add_data'

    data = {
        "table_name": tablename,
        'temp': temp,
        'hum': hum
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending data: {e}")

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print(f"Connecting to network {ssid}...")
        wlan.connect(ssid, password)

        # Wait for connection
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            print("Waiting for connection...")
            led("blick")
            timeout -= 1

    if wlan.isconnected():
        print("Connected!")
        print(f"Network Config: {wlan.ifconfig()}")
        led("on")
    else:
        print("Failed to connect to Wi-Fi.")
        for _ in range(3):
            led("blick", delay=0.5)

def disconnect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.disconnect()
    wlan.active(False)
    for _ in range(4):
        led("blick",0.2)
    # led("off")
    print("Disconnected from network")

# Replace 'your_SSID' and 'your_PASSWORD' with your Wi-Fi credentials
SSID = 'PLAY_Swiatlowod_996A'
PASSWORD = 'n59kGUtsQhp@'

def main():
    while True:
        connect_to_wifi(SSID, PASSWORD)
        # get and send indoor data
        # send_data(tablename="indoor", temp=random.randint(0,99), hum=random.randint(0,99))
        # get and send outdoor data
        send_data(tablename="indoor", temp=random.randint(0,99), hum=random.randint(0,99))

        disconnect_wifi()
        # time.sleep(1800)  # Sleep for 30 minutes
        time.sleep(10)  # Sleep for 10 seconds for test

if __name__ == "__main__":
    main()
