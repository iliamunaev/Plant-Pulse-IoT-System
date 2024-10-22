"""
--- Wi-Fi seup ---

Functions to set up a Wi-Fi station that connects to an external Wi-Fi network and an access point that allows other devices to connect to the ESP32.
ESP32 modes: Station (STA), Access Point (AP)

Created: 22.10.2024
Author: Ilia Munaev
Email: ilyamunaev@gmail.com
"""

import network

# Config for STA (Station)
WIFI_NAME = 'WIFI_NAME'  # Replace with the actual name
WIFI_PASSWORD = 'WIFI_PASSWORD'  # Replace with the actual password

# Config for AP (Access Point)
SSID = 'AP_NAME'
SECURITY = network.AUTH_WPA_WPA2_PSK  # Correct constant for security mode
AP_PASSWORD = 'AP_PASSWORD'


def setup_sta():
    """
    Station aka client, connects to upstream WiFi access points.
    """
    # Initialize the Station interface
    STA = network.WLAN(network.STA_IF)
    
    # Activate the Station mode interface
    STA.active(True)    
    print("\nSTA is active:", STA.active())

    # Connect to a WiFi access point
    STA.connect(WIFI_NAME, WIFI_PASSWORD)

    # Wait for connection to establish
    if STA.isconnected():
        print("STA is connected to Wi-Fi:", STA.isconnected())
        print("STA IP Configuration:", STA.ifconfig())
    else:
        print("Failed to connect to Wi-Fi")
    

def setup_ap():
    """
    Access point, allows other WiFi clients to connect.
    """
    # Initialize the AP interface
    AP = network.WLAN(network.AP_IF)
    
    # Activate the AP mode interface
    AP.active(True)  
    print("AP is active:", AP.active())

    # Configure the AP with WPA2 security protocol
    AP.config(essid=SSID, authmode=SECURITY, password=AP_PASSWORD)
    print("AP IP Configuration:", AP.ifconfig())


def disconnect_sta_ap():
    """ 
    Disconnect from the current network (if connected)
    """
    STA = network.WLAN(network.STA_IF)
    AP = network.WLAN(network.AP_IF)
    
    # Disconnect Station if connected
    if STA.isconnected():
        STA.disconnect()
        print("STA is disconnected from the network:", STA.active())
        
    # Deactivate AP if active
    if AP.active():
        AP.active(False)
        print("AP is deactivated.")