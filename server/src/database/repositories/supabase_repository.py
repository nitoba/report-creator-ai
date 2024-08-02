from http import HTTPStatus

from supabase import Client

from src._common.slugfy import create_slug
from src.contracts.uploader import IUploader, UploadResponse
from src.env import env


class SupabaseRepository(IUploader):
    def __init__(self, supabase_client: Client) -> None:
        self.supabase = supabase_client

    def upload(self, content: str, filename: str) -> UploadResponse:
        result = self.supabase.storage.from_(env.STORAGE_BUCKET).upload(
            file=content,
            path=filename,
            file_options={'content-type': 'text/plain', 'upsert': filename},
        )
        if result.status_code == HTTPStatus.OK:
            return UploadResponse(
                id=result.json()['Key'],
                url=f'{env.SUPABASE_URL}/storage/v1/object/public/{env.STORAGE_BUCKET}/{filename}',
            )
        else:
            result.raise_for_status()

    def upload_to_supabase(self, file_stream: bytes, file_name: str) -> UploadResponse:
        slug = create_slug(file_name)
        response = self.supabase.storage.from_(env.STORAGE_BUCKET).upload(
            path=slug,
            file=file_stream,
            file_options={'content-type': 'text/plain', 'upsert': 'True'},
        )
        if response:
            return UploadResponse(
                id=response.json()['Key'],
                url=f'{env.SUPABASE_URL}/storage/v1/object/public/{env.STORAGE_BUCKET}/{slug}',
            )
        else:
            raise Exception('Falha no upload para o Supabase')
