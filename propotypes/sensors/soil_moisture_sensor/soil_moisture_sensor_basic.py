import machine
import time

# Create ADC object
adc = machine.ADC(machine.Pin(14))
adc.width(machine.ADC.WIDTH_12BIT)  # Set ADC to 12-bit resolution
adc.atten(machine.ADC.ATTN_11DB)    # Set attenuation for full 0-3.3V range

# Assign acctual sensor related values (collibration)
dry, wet = 3260, 1657

# Map raw ADC value to a percentage
def map_value(value, dry, wet, out_min, out_max):
    return (value - dry) * (out_max - out_min) // (wet - dry) + out_min

while True:
    try:
        moisture_value = adc.read()
        if moisture_value < wet:
            moisture_value = wet
        elif moisture_value > dry:
            moisture_value = dry
        
        # Map ADC value to a percentage
        moisture_percent = map_value(moisture_value, dry, wet, 0, 100)

        print("Moisture Value: ", moisture_value, " -> Moisture Percent: ", moisture_percent, "%")

    except OSError as e:
        print("Failed to read from Soil Moisture Sensor", e)

    time.sleep(1)
