# PlantPulse
**PlantPulse** is a plant treatment system using IoT technology. It consists of a central hub (**STM32 Nucleo-64**) and plant stations (**ESP32 WROOM-32**), which collect and monitor environmental data such as soil moisture, temperature, humidity, and light levels. Based on the received data, the system automatically waters the plants. 

**PlantPulse** connects via Wi-Fi and uses MQTT for real-time data transmission between the plant stations and the central hub. This smart system ensures optimal plant care by automating watering based on live environmental conditions.

## Hardware:
- Main Hub: STM32 Nucleo-64 board (C/C++)

- Node: ESP32-WROOM-32 board (C/C++)

- Prototype testing: Arduino Nano ESP32 board (MicroPython)