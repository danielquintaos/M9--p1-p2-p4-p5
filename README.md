# 📡 IoT Sensor Simulator

A modular IoT device simulator using MQTT (via Eclipse Paho), secured with TLS, integrated with HiveMQ, PostgreSQL for persistence, and real-time Metabase dashboards.

Inspired by:
- https://rmnicola.github.io/m9-ec-encontros/ponderada1/
- https://rmnicola.github.io/m9-ec-encontros/ponderada2/
- https://rmnicola.github.io/m9-ec-encontros/ponderada4/
- https://rmnicola.github.io/m9-ec-encontros/ponderada5/

---

## 🌐 Project Overview

This simulator mimics real-world sensors (e.g., SPS30, MiCS-6814, Solar Radiation), publishing JSON data to an MQTT broker. Data is stored in PostgreSQL and visualized with Metabase.

---

## 📦 Features

- ✅ Realistic sensor simulations (with correct units & frequency)
- 🔐 TLS-secured MQTT communication via HiveMQ
- 🧪 Full test suite (QoS, frequency, data integrity, broker connectivity)
- 📊 Dashboard-ready data persistence via PostgreSQL
- 🧰 Built for reproducibility with Nix and optional Docker support
- 🔥 I LOVE THE SMELL OF NAPALM IN THE MORNING!

---

## 🛠️ Supported Sensors

| Sensor              | Type                      | Units    |
|---------------------|---------------------------|----------|
| `sps30`             | Particulate Matter        | µg/m³    |
| `mics6814`          | Gas Sensor (CO, NO₂, NH₃) | ppm      |
| `solar_radiation`   | Solar Radiation           | W/m²     |

---

## 🚀 How to Use (or: Commands in Correct Order)

```bash
# 1. Enter Nix development environment
nix develop

# 2. Enable docker 
nix-shell -p docker-compose

# 3. Start full stack (Postgres + HiveMQ + Metabase)
sudo docker-compose up -d

# 4. Initialize database schema
python scripts/db_migrate.py

# 5. Make shell scripts executable
chmod +x scripts/*.sh  

# 6. Start simulator (choose: sps30, mics6814, solar_radiation)
./scripts/start_simulator.sh sps30

# 7. Run tests (connection, QoS, data integrity, etc.)
./scripts/test_runner.sh
```

## 📸 Video Demo in "demo.mp4"
