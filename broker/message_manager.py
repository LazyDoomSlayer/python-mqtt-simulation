from typing import Callable, Dict

import paho.mqtt.client as mqtt


class MessageHandler:
    """
    Handles incoming MQTT messages and triggers corresponding actions.
    """

    def __init__(self) -> None:
        """Initializes the MessageHandler with an empty action registry."""
        self._actions: Dict[str, Callable[[str], None]] = {}

    def register_action(self, topic: str, action: Callable[[str], None]) -> None:
        """
        Registers a callback action for a specific topic.

        Args:
            topic (str): The MQTT topic.
            action (Callable[[str], None]): The callback function to execute when a message is received on this topic.
        """
        self._actions[topic] = action

    def handle_message(self, client: mqtt.Client, userdata: None, message: mqtt.MQTTMessage) -> None:
        """
        Processes received MQTT messages and triggers the corresponding action.

        Args:
            client (mqtt.Client): The MQTT client instance.
            userdata (None): User-defined data (not used here).
            message (mqtt.MQTTMessage): The received MQTT message.
        """
        topic = message.topic
        payload = message.payload.decode()
        print(f"Received message from topic '{topic}': {payload}")

        # Execute the registered action if available
        if topic in self._actions:
            self._actions[topic](payload)
        else:
            print(f"No action registered for topic: {topic}")
