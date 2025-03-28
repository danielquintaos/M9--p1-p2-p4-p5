# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env if present

def load_config():
    return {
        "MQTT_BROKER": os.getenv("MQTT_BROKER", "broker.hivemq.com"),
        "MQTT_PORT": int(os.getenv("MQTT_PORT", 8883)),
        "MQTT_TOPIC": os.getenv("MQTT_TOPIC", "iot/sensors/sps30"),
        "MQTT_CLIENT_ID": os.getenv("MQTT_CLIENT_ID", "iot-simulator"),
        "MQTT_QOS": int(os.getenv("MQTT_QOS", 1)),

        "TLS_ENABLED": os.getenv("TLS_ENABLED", "true").lower() == "true",
        "TLS_CA": os.getenv("TLS_CA", "certs/ca.pem"),
        "TLS_CERT": os.getenv("TLS_CERT", "certs/client.crt"),
        "TLS_KEY": os.getenv("TLS_KEY", "certs/client.key"),

        "DB_URL": os.getenv("DATABASE_URL", "postgresql://iot_user:password@localhost/iot_data"),
        "PUBLISH_INTERVAL": int(os.getenv("PUBLISH_INTERVAL", 5))
    }
