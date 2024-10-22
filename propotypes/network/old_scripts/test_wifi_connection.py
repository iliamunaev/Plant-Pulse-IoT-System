# !
# This script is DEPRECATED, see wifi_setup.py instead.
# !

"""
--- Test Wi-Fi connection with Arduino Nano ESP32 ---

Created: 17.10.2024
Author: Ilia Munaev
Email: ilyamunaev@gmail.com
"""

import network
import time

WIFI_NETWORK = 'WIFI_NETWORK'  # Replace with the actual name
WIFI_PASSWORD = 'WIFI_PASSWORD'  # Replace with the actual password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_NETWORK, WIFI_PASSWORD)

# Wait until connected or timeout after 10 seconds
max_attempts = 10
attempt = 0

while not wlan.isconnected() and attempt < max_attempts:
    print(f"Attempt {attempt + 1} to connect...")
    time.sleep(1)
    attempt += 1

# Display configs
if wlan.isconnected():
    print("\nConnected to", WIFI_NETWORK)
    print("Network configuration:", wlan.ifconfig())
else:
    print("\nConnection failed")

# Disconnect after 10 sec
print("Disconnection in 10 sec")
time.sleep(10)
wlan.disconnect()
print("Disconnected")