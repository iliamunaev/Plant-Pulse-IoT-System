"""
--- Test Request/Response via Wi-Fi connection ---

Created: 17.10.2024
Author: Ilia Munaev
Email: ilyamunaev@gmail.com
"""
import urequests
import network

# Request a random joke from the Random Joke API
URL = "https://official-joke-api.appspot.com/random_joke"

WIFI_NETWORK = 'NETWORK_NAME'  # Replace with the actual name
WIFI_PASSWORD = 'NETWORK_PASSWORD'  # Replace with the actual password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_NETWORK, WIFI_PASSWORD)

print()
print("Connected to ",WIFI_NETWORK)

response = urequests.get(URL)

print(response.text)