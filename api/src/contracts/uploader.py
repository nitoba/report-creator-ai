from abc import ABC, abstractmethod


class IUploader(ABC):
    @abstractmethod
    def upload(self, content: str, filename: str):
        pass
