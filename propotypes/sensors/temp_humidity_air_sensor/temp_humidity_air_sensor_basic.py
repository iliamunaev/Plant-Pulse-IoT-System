"""
--- Test Temperature/Humidity Air Sensor ---

Created: 20.10.2024
Author: Ilia Munaev
Email: ilyamunaev@gmail.com
"""
import dht
import machine
import time

# Define the pin where the DHT11 is connected with a pull-up resistor enabled
dht_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP) 
sensor = dht.DHT11(dht_pin)
time.sleep(2)

while True:
    try:
        # Read the temperature and humidity from DHT11
        sensor.measure()
        temperature = sensor.temperature()  # Get temperature in Celsius
        humidity = sensor.humidity()        # Get humidity percentage

        # Print the values
        print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))

    except OSError as e:
        print("Failed to read from DHT11 sensor", e)

    time.sleep(2)