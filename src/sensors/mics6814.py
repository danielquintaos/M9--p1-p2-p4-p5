# src/sensors/mics6814.py

import random
import time
from sensors.base_sensor import BaseSensor

class MiCS6814Sensor(BaseSensor):
    def generate_data(self):
        return {
            "timestamp": time.time(),
            "co_ppm": round(random.uniform(0.0, 10.0), 2),      # Carbon Monoxide
            "no2_ppm": round(random.uniform(0.0, 2.0), 3),       # Nitrogen Dioxide
            "nh3_ppm": round(random.uniform(0.0, 5.0), 2),       # Ammonia
        }

    def get_metadata(self):
        return {
            "sensor": "MiCS-6814",
            "units": "ppm",
            "type": "Gas Sensor"
        }
