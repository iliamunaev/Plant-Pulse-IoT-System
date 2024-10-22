"""
--- Make url request ---

Test Request/Response via Wi-Fi connection

Created: 22.10.2024
Author: Ilia Munaev
Email: ilyamunaev@gmail.com
"""
import urequests
import network
from wifi_setup import setup_sta, disconnect_sta_ap

# Make an API request to get a random joke
URL = "https://official-joke-api.appspot.com/random_joke"

def make_url_request(url):

    response = urequests.get(url)

    if response.status_code == 200:
        joke = response.json()
        print("\nHere's a random joke for you:")
        print(joke['setup'])
        print(joke['punchline'])
        response.close()
    else:
        print("\nFailed to retrieve a joke. Status code:", response.status_code)

if __name__ == '__main__':
    # Setup the station connection
    setup_sta()

    # Make the URL request
    make_url_request(URL)

    # Disconnect Wi-Fi
    disconnect_sta_ap()