# src/utils/helpers.py

import random

def bounded_random(low: float, high: float, precision: int = 2) -> float:
    """
    Returns a float with defined precision between low and high.
    """
    return round(random.uniform(low, high), precision)

def simulate_daily_pattern(hour: int, peak_value: float, spread: float = 6.0) -> float:
    """
    Creates a simple bell-like curve based on the time of day.
    Peaks at midday by default (12h).
    """
    peak_hour = 12
    base = -abs(hour - peak_hour) + spread
    return max(0.0, base / spread * peak_value)
