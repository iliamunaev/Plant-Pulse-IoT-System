"""
--- Send and Display Soil Moisture Sensor data via Wi-Fi ---

Created: 22.10.2024
Author: Ilia Munaev
Email: ilyamunaev@gmail.com
"""
import socket
import machine
import network

# ESP32 has a Wi-Fi auto connection. Get the Ip address
wlan = network.WLAN(network.STA_IF)
IP_ADDRESS = wlan.ifconfig()[0]

# Initialize the ADC
adc = machine.ADC(machine.Pin(14))
adc.width(machine.ADC.WIDTH_12BIT)  # Set to 12-bit resolution (0-4095)
adc.atten(machine.ADC.ATTN_11DB)    # Set attenuation for the 0-3.3V range

# Read sensor value
def read_sensor():
    return adc.read()
  
# HTML template for displaying sensor data
def web_page(moisture_value):
    html = """<!DOCTYPE html>
    <html>
        <head>
            <title>ESP32 Sensor Data</title>
            <meta http-equiv="refresh" content="2">
        </head>
        <body>
            <h1>ESP32 Sensor Data</h1>
            <p>Moisture Value: {}</p>
        </body>
    </html>
    """.format(moisture_value)
    
    return html
# Start the web server
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    
    print(f"Server running. Connect to http://{IP_ADDRESS}")

    while True:
        conn, addr = s.accept()
        print('Client connected from', addr)
        request = conn.recv(1024)
        
        # Get the current sensor reading
        moisture_value = read_sensor()  
        
        # Serve the web page with the sensor data
        response = web_page(moisture_value)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

# Run the server
if __name__ == "__main__":
    start_server()