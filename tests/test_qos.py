# tests/test_qos.py

import pytest
from mqtt.publisher import MQTTPublisher
from config import load_config

@pytest.mark.parametrize("qos_level", [0, 1, 2])
def test_mqtt_qos_setting(qos_level):
    config = load_config()
    
    publisher = MQTTPublisher(
        broker=config["MQTT_BROKER"],
        port=config["MQTT_PORT"],
        topic=config["MQTT_TOPIC"],
        client_id=f"test-qos-{qos_level}",
        tls_enabled=config["TLS_ENABLED"],
        tls_ca=config["TLS_CA"],
        tls_cert=config["TLS_CERT"],
        tls_key=config["TLS_KEY"],
        qos=qos_level
    )

    assert publisher.qos == qos_level
