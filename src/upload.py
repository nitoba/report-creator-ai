import io
from os import path

from env import Env
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload

env = Env()

# Caminho para o arquivo de credenciais JSON da conta de serviço
SERVICE_ACCOUNT_FILE = path.dirname(__file__) + '/../credentials.json'

# Definindo escopos de acesso
SCOPES = ['https://www.googleapis.com/auth/drive']

# Autenticação com a conta de serviço
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Criar o serviço do Google Drive
service = build('drive', 'v3', credentials=credentials)


# Função para subir um arquivo para o Google Drive
def upload_file_to_drive(file_path, file_name, folder_id=env.DRIVE_FOLDER_ID):
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    media = MediaFileUpload(file_path, resumable=True)
    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields='id')
        .execute()
    )
    print(
        f"Arquivo '{file_name}' foi enviado com sucesso para o Google Drive. ID do arquivo: {file.get('id')}"
    )


def upload_from_content_to_drive(
    content, file_name, mime_type='text/plain', folder_id=env.DRIVE_FOLDER_ID
):
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    content_io = io.BytesIO(content.encode('utf-8'))

    media = MediaIoBaseUpload(content_io, mimetype=mime_type, resumable=True)
    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields='id')
        .execute()
    )
    print(
        f"Arquivo '{file_name}' foi enviado com sucesso para o Google Drive. ID do arquivo: {file.get('id')}"
    )
