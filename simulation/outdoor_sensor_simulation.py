import json
import time

from broker import MQTTManager
from devices import OutdoorSensor, DeviceType


class OutdoorSensorSimulation:
    def __init__(self, outdoor_sensor: OutdoorSensor, mqtt_manager: MQTTManager):
        self.outdoor_sensor = outdoor_sensor
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the indoor sensor and publish its data."""
        while True:
            self.simulate_step()
            time.sleep(10)  # Simulate every 3 seconds

    def simulate_step(self):
        """Simulate one step for the indoor sensor."""
        if self.outdoor_sensor.powered:
            data = self.outdoor_sensor.generate_data()
            message = {
                "device_type": DeviceType.OUTDOOR_SENSOR.value,
                "data": data,
            }

            topic = f"home/{self.outdoor_sensor.group_id}/{self.outdoor_sensor.device_type}/{self.outdoor_sensor.device_id}/update"
            self.mqtt_manager.publish(topic, json.dumps(message))
        else:
            print(
                f"{self.outdoor_sensor.device_type} {self.outdoor_sensor.device_id} is powered OFF."
            )
