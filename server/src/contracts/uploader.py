from abc import ABC, abstractmethod
from typing import NamedTuple


class UploadResponse(NamedTuple):
    id: str
    url: str


class IUploader(ABC):
    @abstractmethod
    def upload(self, content: str, filename: str) -> UploadResponse:
        pass
