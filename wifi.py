import network
import time
import ubinascii
import requests

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
            time.sleep(1)
            timeout -= 1

    if wlan.isconnected():
        print("Connected!")
        print(f"Network Config: {wlan.ifconfig()}")
    else:
        print("Failed to connect to Wi-Fi.")

# Replace 'your_SSID' and 'your_PASSWORD' with your Wi-Fi credentials
SSID = 'PLAY_Swiatlowod_996A'
PASSWORD = 'n59kGUtsQhp@'

connect_to_wifi(SSID, PASSWORD)

url = 'https://google.com'
resp = requests.get(url)
print(resp.status_code)
print(resp.content)