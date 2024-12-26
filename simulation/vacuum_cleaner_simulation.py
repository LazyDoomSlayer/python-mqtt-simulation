import json
import time

from broker import MQTTManager
from devices import VacuumCleaner, DeviceType


class VacuumCleanerSimulation:
    def __init__(self, vacuum_cleaner: VacuumCleaner, mqtt_manager: MQTTManager):
        self.vacuum_cleaner = vacuum_cleaner
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the vacuum cleaner and publish its commands."""
        while True:
            self.simulate_step()
            time.sleep(30)  # Simulate every 5 seconds

    def simulate_step(self):
        """Simulate one step for the vacuum cleaner."""
        if self.vacuum_cleaner.powered:
            state = self.vacuum_cleaner.generate_state()

            if state["state"] == "Idle":
                self.vacuum_cleaner.start_cleaning()
            else:
                self.vacuum_cleaner.stop_cleaning()

            state = self.vacuum_cleaner.generate_state()
            message = {
                "device_type": DeviceType.VACUUM_CLEANER.value,
                "data": state,
            }

            topic = f"home/{self.vacuum_cleaner.group_id}/{self.vacuum_cleaner.device_type}/{self.vacuum_cleaner.device_id}/command/update"
            self.mqtt_manager.publish(topic, json.dumps(message))
        else:
            print(
                f"{self.vacuum_cleaner.device_type} {self.vacuum_cleaner.device_id} is powered OFF."
            )
