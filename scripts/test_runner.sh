#!/usr/bin/env bash

echo "🧪 Running test suite..."

# Activate env from .env if it exists
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

pytest tests/ --disable-warnings --tb=short "$@"
