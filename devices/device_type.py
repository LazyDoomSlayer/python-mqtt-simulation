from enum import Enum


class DeviceType(Enum):
    """
    Enum for device types to standardize device names across the project.
    """

    ALL_DEVICES = "All devices"
    DOOR_SENSOR = "Door Sensor"
    INDOOR_SENSOR = "Indoor Sensor"
    OUTDOOR_SENSOR = "Outdoor Sensor"
    LIGHT_SWITCH = "Light Switch"
    VACUUM_CLEANER = "Vacuum Cleaner"

    @classmethod
    def list(cls):
        """
        Returns a list of all device names (Enum values).
        """
        return [device.value for device in cls]
