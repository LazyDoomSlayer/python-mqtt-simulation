import json
import time

from broker import MQTTManager
from devices import IndoorSensor, DeviceType


class IndoorSensorSimulation:
    def __init__(self, indoor_sensor: IndoorSensor, mqtt_manager: MQTTManager):
        self.indoor_sensor = indoor_sensor
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the indoor sensor and publish its data."""
        while True:
            self.simulate_step()
            time.sleep(10)  # Simulate every 3 seconds

    def simulate_step(self):
        """Simulate one step for the indoor sensor."""
        if self.indoor_sensor.powered:
            data = self.indoor_sensor.generate_data()

            message = {
                "device_type": DeviceType.INDOOR_SENSOR.value,
                "data": data,
            }

            topic = f"home/{self.indoor_sensor.group_id}/{self.indoor_sensor.device_type}/{self.indoor_sensor.device_id}/update"
            self.mqtt_manager.publish(topic, json.dumps(message))
        else:
            print(
                f"{self.indoor_sensor.device_type} {self.indoor_sensor.device_id} is powered OFF."
            )
