# scripts/validate_hivemq.py

import paho.mqtt.client as mqtt
from config import load_config
from mqtt.tls_config import configure_tls

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Successfully connected to HiveMQ broker.")
    else:
        print(f"❌ Failed to connect, return code: {rc}")

def main():
    config = load_config()

    client = mqtt.Client(client_id="hivemq-validator")
    client.on_connect = on_connect

    if config["TLS_ENABLED"]:
        configure_tls(client, config["TLS_CA"], config["TLS_CERT"], config["TLS_KEY"])

    client.connect(config["MQTT_BROKER"], config["MQTT_PORT"])
    client.loop_start()

if __name__ == "__main__":
    main()
