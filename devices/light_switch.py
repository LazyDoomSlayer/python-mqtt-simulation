from devices.device import Device


class LightSwitch(Device):
    def __init__(self, group_id, device_id, mqtt_manager):
        super().__init__(group_id, "light_switch", device_id)
        self.mqtt_manager = mqtt_manager
        self.state = "OFF"

    def toggle(self):
        """Toggle the state of the light switch."""
        self.state = "ON" if self.state == "OFF" else "OFF"

    def set_state(self, state):
        """Set the light switch to a specific state."""
        self.state = state

    def generate_state(self):
        """Generate the current state of the light switch."""
        return {"state": self.state}
