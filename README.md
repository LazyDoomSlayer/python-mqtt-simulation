# Python MQTT Simulation

## Overview

This project simulates multiple IoT devices communicating with an MQTT broker. It allows users to simulate device
behavior, publish data to MQTT topics, and monitor messages. The project is modular and extensible, supporting different
device types and easy customization.

## Features

- **Device Simulation**: Simulates multiple devices, including sensors and actuators.
- **MQTT Integration**: Publishes and subscribes to topics using an MQTT broker.
- **Device Management**: Supports multiple device types like:
    - **Door Sensor**
    - **Indoor Sensor**
    - **Outdoor Sensor**
    - **Light Switch**
    - **Vacuum Cleaner**
- **Interactive Selection**: Choose to simulate a single device or all devices.
- **Multithreading**: Allows concurrent simulation of all devices.

---

## Installation

### Prerequisites

- Python 3.8 or later
- `pip` package manager
- An MQTT broker (e.g., Mosquitto or HiveMQ)
- [paho](https://pypi.org/project/paho-mqtt/) : client library for mqtt

```
pip install paho-mqtt
```

- [Curses](https://pypi.org/project/windows-curses/) : menu selector for simulation options

```
pip install windows-curses
```

- mosquitto installation for **debian**

```
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

- mosquitto installation for **red-hat based**

```
sudo dnf install -y mosquitto mosquitto-clients
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
```

- mosquitto installation for **macos**

```
brew install mosquitto
brew services start mosquitto
```

- [mosquitto](https://mosquitto.org/download/) installation for **windows**

## Structure

```
python-mqtt-simulation/
├── broker/
│   ├── mqtt_manager.py          # Manages MQTT connections and messaging
├── devices/
│   ├── device.py                # Base class for all devices
│   ├── door_sensor.py           # Door sensor implementation
│   ├── indoor_sensor.py         # Indoor sensor implementation
│   ├── outdoor_sensor.py        # Outdoor sensor implementation
│   ├── light_switch.py          # Light switch implementation
│   ├── vacuum_cleaner.py        # Vacuum cleaner implementation
├── menu/
│   ├── device_selector.py       # Handles user device selection
├── simulation/
│   ├── simulation_controller.py # Controls simulations for all devices
│   ├── door_sensor_simulation.py # Door sensor simulation logic
│   ├── indoor_sensor_simulation.py # Indoor sensor simulation logic
│   ├── outdoor_sensor_simulation.py # Outdoor sensor simulation logic
│   ├── light_switch_simulation.py # Light switch simulation logic
│   ├── vacuum_cleaner_simulation.py # Vacuum cleaner simulation logic
├── main.py                      # Entry point for the simulation
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
```

## To run use following command:

```
python main.py
```

## To verify publishing of messages

```
mosquitto_sub -h <BROKER_IP> -t "home/#"
```