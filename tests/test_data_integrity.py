# tests/test_data_integrity.py

import pytest
from sensors.sps30 import SPS30Sensor
from sensors.mics6814 import MiCS6814Sensor
from sensors.solar_radiation import SolarRadiationSensor

@pytest.mark.parametrize("sensor_class, expected_fields", [
    (SPS30Sensor, ["pm1_0", "pm2_5", "pm4_0", "pm10"]),
    (MiCS6814Sensor, ["co_ppm", "no2_ppm", "nh3_ppm"]),
    (SolarRadiationSensor, ["irradiance"]),
])
def test_sensor_output_integrity(sensor_class, expected_fields):
    sensor = sensor_class()
    data = sensor.generate_data()

    assert isinstance(data, dict)
    assert "timestamp" in data
    for field in expected_fields:
        assert field in data
        assert isinstance(data[field], float)
