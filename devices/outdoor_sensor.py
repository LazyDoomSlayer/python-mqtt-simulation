from devices.device import Device

import random

class OutdoorSensor(Device):
    def __init__(self, group_id, device_id, mqtt_manager):
        super().__init__(group_id, "outdoor_sensor", device_id)
        self.mqtt_manager = mqtt_manager

    def read_humidity(self):
        """Generate and return simulated humidity data."""
        return random.uniform(20.0, 80.0)  # Humidity in %

    def read_temperature(self):
        """Generate and return simulated temperature data."""
        return random.uniform(-10.0, 40.0)  # Temperature in °C

    def generate_data(self):
        """Combine humidity and temperature readings into a dictionary."""
        return {
            "humidity": self.read_humidity(),
            "temperature": self.read_temperature(),
        }