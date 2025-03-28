# src/mqtt/publisher.py

import json
import ssl
import time
import paho.mqtt.client as mqtt
from utils.logger import get_logger
from mqtt.tls_config import configure_tls

logger = get_logger("MQTT Publisher")


class MQTTPublisher:
    def __init__(self, broker, port, topic, client_id, tls_enabled=False, tls_ca=None, tls_cert=None, tls_key=None, qos=1):
        self.topic = topic
        self.qos = qos
        self.client = mqtt.Client(client_id=client_id)
        self.client.on_connect = self._on_connect
        self.client.on_publish = self._on_publish

        if tls_enabled:
            configure_tls(self.client, tls_ca, tls_cert, tls_key)

        self.client.connect(broker, port)
        self.client.loop_start()
        time.sleep(1)  # Give time to establish connection

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT broker successfully.")
        else:
            logger.error(f"Failed to connect, return code {rc}")

    def _on_publish(self, client, userdata, mid):
        logger.debug(f"Message {mid} published to topic {self.topic}")

    def publish(self, data: dict):
        payload = json.dumps(data)
        result = self.client.publish(self.topic, payload, qos=self.qos)
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            logger.error(f"Publish failed with code: {result.rc}")
