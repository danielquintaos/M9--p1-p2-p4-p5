# src/mqtt/subscriber.py

import ssl
import paho.mqtt.client as mqtt
from utils.logger import get_logger
from mqtt.tls_config import configure_tls

logger = get_logger("MQTT Subscriber")


class MQTTSubscriber:
    def __init__(self, broker, port, topic, client_id, tls_enabled=False, tls_ca=None, tls_cert=None, tls_key=None, qos=1, on_message=None):
        self.topic = topic
        self.client = mqtt.Client(client_id=client_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = on_message or self._on_message

        if tls_enabled:
            configure_tls(self.client, tls_ca, tls_cert, tls_key)

        self.client.connect(broker, port)
        self.client.loop_start()

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info(f"Subscriber connected. Subscribing to {self.topic}")
            self.client.subscribe(self.topic)
        else:
            logger.error(f"Subscriber failed to connect, return code {rc}")

    def _on_message(self, client, userdata, msg):
        logger.info(f"Received message on {msg.topic}: {msg.payload.decode()}")
