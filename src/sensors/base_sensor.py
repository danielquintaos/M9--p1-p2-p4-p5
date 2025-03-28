# src/sensors/base_sensor.py

from abc import ABC, abstractmethod


class BaseSensor(ABC):
    """
    Abstract base class for all sensor simulators.
    """

    @abstractmethod
    def generate_data(self) -> dict:
        """
        Generate a single sensor data payload as a dictionary.
        Must be implemented by child sensor classes.
        """
        pass

    def get_metadata(self) -> dict:
        """
        Optional: Metadata about the sensor (type, units, etc.)
        """
        return {}
