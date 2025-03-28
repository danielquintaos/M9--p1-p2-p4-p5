#!/usr/bin/env bash

set -e

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

SENSOR=${1:-sps30}

echo "🚀 Starting simulator for sensor: $SENSOR"
python3 src/main.py --sensor "$SENSOR"
