#!/bin/sh
set -e

# Run migrations
alembic upgrade head

# Start the application
exec fastapi run src/http/app.py --host 0.0.0.0 --port ${PORT}
