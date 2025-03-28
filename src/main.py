# src/main.py

import time
import argparse

from sensors.sps30 import SPS30Sensor  # Replace with desired sensor module
from mqtt.publisher import MQTTPublisher
from config import load_config
from utils.logger import get_logger

logger = get_logger("main")


def run_simulator(sensor_type: str):
    config = load_config()

    # Initialize MQTT publisher
    mqtt_publisher = MQTTPublisher(
        broker=config["MQTT_BROKER"],
        port=config["MQTT_PORT"],
        topic=config["MQTT_TOPIC"],
        client_id=config["MQTT_CLIENT_ID"],
        tls_enabled=config["TLS_ENABLED"],
        tls_ca=config["TLS_CA"],
        tls_cert=config["TLS_CERT"],
        tls_key=config["TLS_KEY"],
        qos=config["MQTT_QOS"]
    )

    # Select and initialize sensor simulator
    if sensor_type.lower() == "sps30":
        sensor = SPS30Sensor()
    else:
        raise ValueError(f"Unsupported sensor type: {sensor_type}")

    # Begin simulation loop
    interval = config.get("PUBLISH_INTERVAL", 5)
    logger.info(f"Starting {sensor_type} simulator with {interval}s interval.")

    while True:
        data = sensor.generate_data()
        mqtt_publisher.publish(data)
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IoT Sensor Simulator")
    parser.add_argument("--sensor", type=str, required=True, help="Sensor type (e.g., sps30)")

    args = parser.parse_args()

    try:
        run_simulator(args.sensor)
    except KeyboardInterrupt:
        logger.info("Simulator stopped by user.")
