class Device:
    def __init__(self, group_id, device_type, device_id):
        self.group_id = group_id
        self.device_type = device_type
        self.device_id = device_id
        self.powered = False

    def is_powered_on(self) -> bool:
        return self.powered

    def power_on(self):
        """Turn on the device."""
        self.powered = True
        print(f"{self.device_type} {self.device_id} powered ON.")

    def power_off(self):
        """Turn off the device."""
        self.powered = False
        print(f"{self.device_type} {self.device_id} powered OFF.")
