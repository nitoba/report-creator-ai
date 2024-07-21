FROM python:3.12.4-slim AS build

COPY ./requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libpq-dev gcc && python3 -m venv /venv

ENV PATH=/venv/bin:$PATH

RUN pip3 install --no-cache-dir -r requirements.txt

FROM python:3.12.4-slim AS runtime

COPY --from=build /venv /venv
ENV PATH=/venv/bin:$PATH


# Definir variáveis de ambiente
ENV OPEN_AI_KEY=your_open_ai_key
ENV OPEN_AI_BASE_URL=your_open_ai_base_url
ENV CHAT_MODEL=your_chat_model
ENV EMBEDDING_MODEL=your_embedding_model
ENV DRIVE_FOLDER_ID=your_drive_folder_id
ENV DISCORD_CHANNEL_ID=your_discord_channel_id
ENV DISCORD_TOKEN=your_discord_token
ENV GOOGLE_SERVICE_ACCOUNT_TYPE=test
ENV GOOGLE_PROJECT_ID=test
ENV GOOGLE_PRIVATE_KEY_ID=test
ENV GOOGLE_PRIVATE_KEY=test
ENV GOOGLE_CLIENT_EMAIL=test
ENV GOOGLE_CLIENT_ID=test
ENV GOOGLE_AUTH_URI=test
ENV GOOGLE_TOKEN_URI=test
ENV GOOGLE_AUTH_PROVIDER_X509_CERT_URL=test
ENV GOOGLE_CLIENT_X509_CERT_URL=test
ENV PORT=3333


WORKDIR /app

COPY . .

EXPOSE ${PORT}

ENTRYPOINT uvicorn src.http.app:app --host 0.0.0.0 --port ${PORT}