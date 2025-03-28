# src/sensors/sps30.py

import random
import time
from sensors.base_sensor import BaseSensor

class SPS30Sensor(BaseSensor):
    def generate_data(self):
        return {
            "timestamp": time.time(),
            "pm1_0": round(random.uniform(0.0, 15.0), 2),   # µg/m3
            "pm2_5": round(random.uniform(0.0, 35.0), 2),   # µg/m3
            "pm4_0": round(random.uniform(0.0, 50.0), 2),   # µg/m3
            "pm10": round(random.uniform(0.0, 100.0), 2),   # µg/m3
        }

    def get_metadata(self):
        return {
            "sensor": "SPS30",
            "units": "µg/m3",
            "type": "Particulate Matter Sensor"
        }
