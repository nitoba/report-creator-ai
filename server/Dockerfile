FROM python:3.12.4-slim AS build

COPY ./requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip3 install --no-cache-dir --target=packages -r requirements.txt

FROM python:3.12.4-alpine AS runtime

COPY --from=build packages /usr/lib/python3.12.4/site-packages
ENV PYTHONPATH=/usr/lib/python3.12.4/site-packages

# Security Context 
RUN useradd -m nonroot
USER nonroot

# Env configuration [ Step 6 ]
WORKDIR /app

COPY . .

EXPOSE 3333

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3333"]