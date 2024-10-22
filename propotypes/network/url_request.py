# !
# This script is DEPRECATED, see wifi_setup.py instead.
# !

"""
--- Test Request/Response via Wi-Fi connection ---

Created: 17.10.2024
Author: Ilia Munaev
Email: ilyamunaev@gmail.com
"""
import urequests
import network

# Setup connectionto Wi-Fi
WIFI_NAME = 'WIFI_NAME'  # Replace with the actual name
WIFI_PASSWORD = 'WIFI_PASSWORD'  # Replace with the actual password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_NAME, WIFI_PASSWORD)

print("\nConnected to ", WIFI_NAME)

# Make an API request to get a random joke
url = "https://official-joke-api.appspot.com/random_joke"

response = urequests.get(url)

if response.status_code == 200:
    joke = response.json()
    print("\nHere's a random joke for you:")
    print(joke['setup'])
    print(joke['punchline'])
    response.close()
else:
    print("\nFailed to retrieve a joke. Status code:", response.status_code)