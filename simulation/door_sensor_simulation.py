import json
import time

from broker import MQTTManager
from devices import DoorSensor, DeviceType


class DoorSensorSimulation:
    def __init__(self, door_sensor: DoorSensor, mqtt_manager: MQTTManager):
        self.door_sensor = door_sensor
        self.mqtt_manager = mqtt_manager

    def simulate(self) -> None:
        """Simulate the door sensor and publish its state."""
        while True:
            self.simulate_step()
            time.sleep(20)

    def simulate_step(self) -> None:
        """Simulate one step for the door sensor."""

        state = self.door_sensor.generate_state()
        if state["state"] == "open":
            self.door_sensor.close_door()
        else:
            self.door_sensor.open_door()

        state = self.door_sensor.generate_state()

        message = {
            "device_type": DeviceType.INDOOR_SENSOR.value,
            "data": state,
        }

        topic = f"home/{self.door_sensor.group_id}/{self.door_sensor.device_type}/{self.door_sensor.device_id}/state/update"
        self.mqtt_manager.publish(topic, json.dumps(message))
