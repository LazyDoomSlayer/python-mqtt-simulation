from typing import Callable

import paho.mqtt.client as mqtt

from .message_manager import MessageHandler


class MQTTManager:
    """
    Manages MQTT broker connection, subscriptions, and message publishing.
    """

    def __init__(self) -> None:
        """Initializes MQTTManager with broker configuration and an MQTT client."""
        self._configure_broker()

        self.client: mqtt.Client = mqtt.Client()
        self.message_handler = MessageHandler()

    def _configure_broker(self) -> None:
        """
        Prompts the user for broker address and port configuration.
        """
        self.broker = input("Enter the MQTT broker address (e.g., localhost): ").strip()
        try:
            self.port = int(
                input("Enter the MQTT broker port (default: 1883): ").strip()
            )
        except ValueError:
            print("Invalid input. Defaulting to port 1883.")
            self.port = 1883

        print(f"Configured MQTT broker: {self.broker}:{self.port}")

    def connect(self) -> None:
        """
        Connects to the configured MQTT broker.
        """
        try:
            self.client.connect(self.broker, self.port)
            print(f"Connected to MQTT broker at {self.broker}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to broker: {e}")

    def subscribe(self, topic: str, action: Callable[[str], None]) -> None:
        """
        Subscribes to a topic and registers an action to handle its messages.

        Args:
            topic (str): The MQTT topic to subscribe to.
            action (Callable[[str], None]): The callback function to execute when a message is received.
        """
        self.message_handler.register_action(topic, action)
        self.client.subscribe(topic)
        self.client.on_message = self.message_handler.handle_message
        print(f"Subscribed to topic: {topic}")

    def publish(self, topic: str, message: str) -> None:
        """
        Publishes a message to a topic.

        Args:
            topic (str): The MQTT topic to publish to.
            message (str): The message payload.
        """
        self.client.publish(topic, message)
        print(f"Published to {topic}: {message}")

    def start(self) -> None:
        """
        Starts the MQTT loop to process incoming and outgoing messages.
        """
        print("MQTT loop started.")
        self.client.loop_start()

    def stop(self) -> None:
        """
        Stops the MQTT loop and disconnects from the broker.
        """
        print("Stopping MQTT loop and disconnecting...")
        self.client.loop_stop()
        self.client.disconnect()
        print("MQTT loop stopped and disconnected.")
