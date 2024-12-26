from devices.device import Device


class DoorSensor(Device):
    def __init__(self, group_id, device_id, mqtt_manager):
        super().__init__(group_id, "door_sensor", device_id)
        self.mqtt_manager = mqtt_manager
        self.state = "CLOSED"

    def generate_state(self):
        """Generate the current state of the door."""
        return {"state": self.state}

    def open_door(self):
        self.state = "OPEN"

    def close_door(self):
        self.state = "CLOSED"
