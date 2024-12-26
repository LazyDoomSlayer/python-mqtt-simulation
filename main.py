import threading
import time

from broker import MQTTManager
from devices import DeviceType
from devices import (
    DoorSensor,
    IndoorSensor,
    LightSwitch,
    VacuumCleaner,
)
from menu import DeviceSelector
from simulation import (
    IndoorSensorSimulation,
    LightSwitchSimulation,
    OutdoorSensorSimulation,
    VacuumCleanerSimulation,
    DoorSensorSimulation,
)


def main():
    """
    Main function to initialize the MQTT manager, handle user input, and control simulations.
    """
    print("=== MQTT Broker Connection ===")

    # Step 1: Initialize the MQTT Manager (prompts user for broker details)
    mqtt_manager = MQTTManager()
    mqtt_manager.connect()
    mqtt_manager.start()

    time.sleep(2)

    indoor_sensor = IndoorSensor("group1", "device1", mqtt_manager)
    light_switch = LightSwitch("group1", "device2", mqtt_manager)
    vacuum_cleaner = VacuumCleaner("group1", "device3", mqtt_manager)

    outdoor_sensor = IndoorSensor("group2", "device4", mqtt_manager)
    door_sensor = DoorSensor("group2", "device5", mqtt_manager)

    print("Starting to power on devices.")
    door_sensor.power_on()
    indoor_sensor.power_on()
    outdoor_sensor.power_on()
    light_switch.power_on()
    vacuum_cleaner.power_on()

    time.sleep(2)

    selection = DeviceSelector()
    device_selected = selection.get_selection()

    # Devices and their corresponding simulation classes
    device_simulations = {
        DeviceType.DOOR_SENSOR.value: (door_sensor, DoorSensorSimulation),
        DeviceType.INDOOR_SENSOR.value: (indoor_sensor, IndoorSensorSimulation),
        DeviceType.OUTDOOR_SENSOR.value: (outdoor_sensor, OutdoorSensorSimulation),
        DeviceType.LIGHT_SWITCH.value: (light_switch, LightSwitchSimulation),
        DeviceType.VACUUM_CLEANER.value: (vacuum_cleaner, VacuumCleanerSimulation),
    }
    threads = []
    if device_selected == DeviceType.ALL_DEVICES.value:
        print("Starting simulation for all devices... Press Ctrl+C to stop.")

        for _, (device, simulation_class) in device_simulations.items():
            thread = threading.Thread(
                target=start_simulation, args=(device, simulation_class, mqtt_manager)
            )
            thread.daemon = True
            threads.append(thread)
            thread.start()

    else:
        device, simulation_class = device_simulations[device_selected]
        thread = threading.Thread(
            target=start_simulation, args=(device, simulation_class, mqtt_manager)
        )
        thread.daemon = True
        threads.append(thread)
        thread.start()

    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")

    mqtt_manager.stop()


def start_simulation(device, simulation_class, mqtt_manager):
    """
    Start simulation for a single device in a thread.

    Args:
        device: The device instance.
        simulation_class: The simulation class to use.
        mqtt_manager: The MQTTManager instance.
    """
    simulation = simulation_class(device, mqtt_manager)
    simulation.simulate()


if __name__ == "__main__":
    main()
