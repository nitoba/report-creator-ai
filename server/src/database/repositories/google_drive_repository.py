import io
import re

import chardet
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload

from src.contracts.uploader import IUploader, UploadResponse
from src.env import env

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

    def upload(self, content: str, filename: str) -> UploadResponse:
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
            file_id = file.get('id')
            print(file)
            print(
                f"Arquivo '{filename}' foi enviado com sucesso para o Google Drive. ID do arquivo: {file.get('id')}"
            )
            return UploadResponse(id=file.get('id'), url='')
        except Exception as err:
            print(err)
            raise err

    def list_files_in_folder(self) -> list:
        results = (
            self.client.files()
            .list(
                q=f"'{env.DRIVE_FOLDER_ID}' in parents and mimeType != 'application/vnd.google-apps.folder'",
                pageSize=10,
                fields='files(id, name, mimeType)',
            )
            .execute()
        )
        return results.get('files', [])

    def download_file(self, file_id: str, mime_type: str) -> io.BytesIO:
        request = self.client.files().export_media(
            fileId=file_id,
            mimeType='text/plain',
        )

        file_stream = io.BytesIO()
        downloader = MediaIoBaseDownload(file_stream, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        file_stream.seek(0)  # Move the cursor to the beginning of the stream
        return file_stream

    def count_words_in_file(file_stream: io.BytesIO) -> int:
        file_stream.seek(0)  # Ensure we're reading from the start of the stream
        content_bytes = file_stream.read()

        # Detectar a codificação do conteúdo
        result = chardet.detect(content_bytes)
        encoding = result['encoding']

        if not encoding:
            raise UnicodeDecodeError('Não foi possível detectar a codificação do arquivo')

        content = content_bytes.decode(encoding)
        return len(re.findall(r'\w+', content))
