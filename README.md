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

### 📂 Project Folder Structure

```text
iot-simulator/
├── README.md                  # 📘 Project overview and usage instructions
├── flake.nix                  # 🧊 Nix flake defining the dev environment
├── flake.lock                 # 🔒 Lock file for reproducible builds
├── shell.nix                  # 🐚 Fallback dev shell (non-flake compatible)
├── .env                       # 🔐 Environment variables (not committed)
├── .gitignore                 # 🙈 Git exclusions (e.g., .env, __pycache__)
│
├── src/                       # 💡 Main application source code
│   ├── __init__.py
│   ├── main.py                # 🚀 Entry point for the simulator (CLI-based)
│   ├── config.py              # ⚙️ Loads MQTT, DB, TLS configs from .env
│
│   ├── mqtt/                  # 📡 MQTT communication logic
│   │   ├── __init__.py
│   │   ├── publisher.py       # Publishes sensor data to broker
│   │   ├── subscriber.py      # (Optional) Receives messages for test/monitoring
│   │   └── tls_config.py      # TLS setup (CA, certs) for secure MQTT
│
│   ├── sensors/               # 🔬 Sensor simulation logic
│   │   ├── __init__.py
│   │   ├── base_sensor.py     # Abstract class for all sensors
│   │   ├── sps30.py           # Simulates SPS30 particulate sensor
│   │   ├── mics6814.py        # Simulates MiCS-6814 gas sensor
│   │   └── solar_radiation.py # Simulates solar irradiance sensor
│
│   ├── persistence/           # 💾 Data storage and ORM layer
│   │   ├── __init__.py
│   │   ├── database.py        # SQLAlchemy session/engine setup
│   │   └── models.py          # SensorData model definition (JSON-based)
│
│   └── utils/                 # 🧰 Utility functions and helpers
│       ├── logger.py          # Standardized logging formatter
│       └── helpers.py         # Random generators, time-based simulators, etc.
│
├── tests/                     # ✅ Pytest-based test suite
│   ├── __init__.py
│   ├── test_mqtt_connection.py  # Tests broker reachability & TLS config
│   ├── test_data_integrity.py   # Asserts valid sensor output format
│   ├── test_frequency.py        # Confirms publish interval is accurate
│   └── test_qos.py              # Verifies configured MQTT QoS level
│
├── nix/                       # 🧪 Nix-based environment config
│   ├── default.nix            # Standalone Python + dependency setup
│   ├── python-packages.nix    # Explicit version pinning for Python libs
│   └── services.nix           # Optional: NixOS config for running Postgres locally
│
├── scripts/                   # 🖥️ CLI helpers and dev automation
│   ├── start_simulator.sh     # Starts the simulator with sensor arg
│   ├── test_runner.sh         # Runs full test suite
│   ├── db_migrate.py          # Creates tables in PostgreSQL
│   └── validate_hivemq.py     # Verifies broker/TLS connectivity
│
└── dashboards/                # 📊 Metabase visualization config
    └── metabase/
        ├── dashboard.json     # Exported Metabase dashboard file
        └── setup_guide.md     # Step-by-step instructions to connect Metabase
```

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
