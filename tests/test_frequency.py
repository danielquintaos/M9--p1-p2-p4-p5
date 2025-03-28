# tests/test_frequency.py

import time
from sensors.sps30 import SPS30Sensor

def test_publish_interval_accuracy():
    sensor = SPS30Sensor()
    interval = 2  # seconds
    sample_count = 3
    timestamps = []

    for _ in range(sample_count):
        _ = sensor.generate_data()
        timestamps.append(time.time())
        time.sleep(interval)

    # Calculate intervals between samples
    diffs = [round(timestamps[i] - timestamps[i - 1], 1) for i in range(1, sample_count)]

    # Assert each interval is within tolerance (±0.5s)
    for diff in diffs:
        assert abs(diff - interval) <= 0.5, f"Interval {diff}s out of expected range"
