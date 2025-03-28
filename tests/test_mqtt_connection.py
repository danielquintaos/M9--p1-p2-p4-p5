# tests/test_mqtt_connection.py

import pytest
from mqtt.publisher import MQTTPublisher
from config import load_config

@pytest.fixture
def mqtt_config():
    return load_config()

def test_mqtt_tls_connection(mqtt_config):
    try:
        publisher = MQTTPublisher(
            broker=mqtt_config["MQTT_BROKER"],
            port=mqtt_config["MQTT_PORT"],
            topic=mqtt_config["MQTT_TOPIC"],
            client_id="test-connection",
            tls_enabled=mqtt_config["TLS_ENABLED"],
            tls_ca=mqtt_config["TLS_CA"],
            tls_cert=mqtt_config["TLS_CERT"],
            tls_key=mqtt_config["TLS_KEY"],
            qos=1
        )
        assert publisher.client.is_connected() is True
    except Exception as e:
        pytest.fail(f"MQTT TLS connection failed: {e}")
