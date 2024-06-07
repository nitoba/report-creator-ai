from os import path

from contracts.content_handler import IContentHandler


class FileHandlerRepository(IContentHandler):
    def __init__(self, directory: str):
        self.directory = directory

    def get_content(self, filename: str) -> str:
        filepath = path.join(self.directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
