from abc import ABC, abstractmethod


class IContentHandler(ABC):
    @abstractmethod
    def get_content(self, filename: str) -> str:
        pass
