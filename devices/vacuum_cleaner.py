from enum import Enum

from devices.device import Device


class VacuumCleanerState(Enum):
    """
    Enum for vacuum cleaner state.
    """

    IDLE = "Idle"
    CLEANING = "Cleaning"


class VacuumCleaner(Device):
    def __init__(self, group_id, device_id, mqtt_manager):
        super().__init__(group_id, "vacuum_cleaner", device_id)
        self.mqtt_manager = mqtt_manager
        self.state = VacuumCleanerState.IDLE

    def start_cleaning(self):
        """Start the vacuum cleaner."""
        self.state = VacuumCleanerState.CLEANING

    def stop_cleaning(self):
        """Stop the vacuum cleaner."""
        self.state = VacuumCleanerState.IDLE

    def generate_state(self):
        """Generate the current state of    the vacuum cleaner."""
        return {"state": self.state.value}
