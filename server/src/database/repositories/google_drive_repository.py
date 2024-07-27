import io
from os import path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

from src.contracts.uploader import IUploader
from src.env import env

SERVICE_ACCOUNT_FILE = f'{path.dirname(__file__)}/../../credentials.json'

SCOPES = ['https://www.googleapis.com/auth/drive']


class GoogleDriveRepository(IUploader):
    def __init__(self) -> None:
        service_account_info = {
            'type': env.GOOGLE_SERVICE_ACCOUNT_TYPE,
            'project_id': env.GOOGLE_PROJECT_ID,
            'private_key_id': env.GOOGLE_PRIVATE_KEY_ID,
            'private_key': env.GOOGLE_PRIVATE_KEY.replace('\\n', '\n'),
            'client_email': env.GOOGLE_CLIENT_EMAIL,
            'client_id': env.GOOGLE_CLIENT_ID,
            'auth_uri': env.GOOGLE_AUTH_URI,
            'token_uri': env.GOOGLE_TOKEN_URI,
            'auth_provider_x509_cert_url': env.GOOGLE_AUTH_PROVIDER_X509_CERT_URL,
            'client_x509_cert_url': env.GOOGLE_CLIENT_X509_CERT_URL,
        }
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info, scopes=SCOPES
        )
        self.client = build('drive', 'v3', credentials=credentials)

    def upload(self, content: str, filename: str):
        file_metadata = {
            'name': filename,
            'parents': [env.DRIVE_FOLDER_ID],
            'mimeType': 'application/vnd.google-apps.document',
        }

        content_io = io.BytesIO(content.encode('utf-8'))

        media = MediaIoBaseUpload(content_io, mimetype='text/plain', resumable=True)
        try:
            file = (
                self.client.files()
                .create(body=file_metadata, media_body=media, fields='id')
                .execute()
            )
            print(
                f"Arquivo '{filename}' foi enviado com sucesso para o Google Drive. ID do arquivo: {file.get('id')}"
            )
            return f"Arquivo '{filename}' foi enviado com sucesso para o Google Drive. ID do arquivo: {file.get('id')}"
        except Exception as err:
            print(err)
            raise err
