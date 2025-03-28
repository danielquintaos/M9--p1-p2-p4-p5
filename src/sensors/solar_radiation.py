# src/sensors/solar_radiation.py

import random
import time
from sensors.base_sensor import BaseSensor

class SolarRadiationSensor(BaseSensor):
    def generate_data(self):
        # Simulate daily light curve with fluctuation
        hour = time.localtime().tm_hour
        base_radiation = max(0, (-abs(hour - 12) + 6) * 100)  # peaks at noon
        variation = random.uniform(-50, 50)
        radiation = max(0, base_radiation + variation)

        return {
            "timestamp": time.time(),
            "irradiance": round(radiation, 1)  # W/m²
        }

    def get_metadata(self):
        return {
            "sensor": "Hobonet RXW-LIB-900",
            "units": "W/m²",
            "type": "Solar Radiation Sensor"
        }
