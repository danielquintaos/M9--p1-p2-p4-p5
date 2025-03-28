# src/persistence/handler.py

from persistence.database import SessionLocal
from persistence.models import SensorData

def save_sensor_data(sensor_type: str, data: dict):
    session = SessionLocal()
    try:
        record = SensorData(sensor_type=sensor_type, payload=data)
        session.add(record)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"[DB] Error saving data: {e}")
    finally:
        session.close()
