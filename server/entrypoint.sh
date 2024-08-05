#!/bin/sh
set -e

# Run migrations
alembic upgrade head

# Start the application
exec uvicorn src.http.app:app --host 0.0.0.0 --port ${PORT}
