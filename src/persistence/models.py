# src/persistence/models.py

from sqlalchemy import Column, Integer, String, Float, JSON, DateTime
from datetime import datetime
from persistence.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
