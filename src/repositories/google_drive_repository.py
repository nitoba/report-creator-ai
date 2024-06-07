import io
from os import path

from contracts.uploader import IUploader
from env import Env
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

env = Env()

SERVICE_ACCOUNT_FILE = path.dirname(__file__) + '/../../credentials.json'

SCOPES = ['https://www.googleapis.com/auth/drive']


class GoogleDriveRepository(IUploader):
    def __init__(self) -> None:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        self.service = build('drive', 'v3', credentials=credentials)

    @classmethod
    def upload(self, content: str, filename: str):
        file_metadata = {'name': filename}
        file_metadata['parents'] = env.DRIVE_FOLDER_ID

        content_io = io.BytesIO(content.encode('utf-8'))

        media = MediaIoBaseUpload(content_io, mimetype='text/plain', resumable=True)
        file = (
            self.service.files()
            .create(body=file_metadata, media_body=media, fields='id')
            .execute()
        )
        print(
            f"Arquivo '{filename}' foi enviado com sucesso para o Google Drive. ID do arquivo: {file.get('id')}"
        )
