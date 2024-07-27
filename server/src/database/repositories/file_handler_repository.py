from os import path

from src.contracts.content_handler import IContentHandler


class FileHandlerRepository(IContentHandler):
    def __init__(self, directory: str):
        self.directory = directory

    def get_content(self) -> str:
        filepath = path.join(self.directory, 'report.txt')
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
