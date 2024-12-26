import json
import time

from broker import MQTTManager
from devices import LightSwitch, DeviceType


class LightSwitchSimulation:
    def __init__(self, light_switch: LightSwitch, mqtt_manager: MQTTManager):
        self.light_switch = light_switch
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the light switch and publish its state."""
        while True:
            self.simulate_step()
            time.sleep(15)  # Simulate every 4 seconds

    def simulate_step(self):
        """Simulate one step for the light switch."""
        if self.light_switch.powered:
            self.light_switch.toggle()
            state = self.light_switch.generate_state()

            message = {
                "device_type": DeviceType.LIGHT_SWITCH.value,
                "data": state,
            }

            topic = f"home/{self.light_switch.group_id}/{self.light_switch.device_type}/{self.light_switch.device_id}/state/update"
            self.mqtt_manager.publish(topic, json.dumps(message))
        else:
            print(
                f"{self.light_switch.device_type} {self.light_switch.device_id} is powered OFF."
            )
