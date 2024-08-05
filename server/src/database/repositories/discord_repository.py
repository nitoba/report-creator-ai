from http import HTTPStatus

from requests import api

from src.contracts.content_handler import IContentHandler
from src.env import env


class DiscordRepository(IContentHandler):
    def __init__(self) -> None:
        self.base_url = 'https://discord.com/api/v10/channels'

    def get_content(self) -> str:
        result = ''
        response = api.get(
            f'{self.base_url}/{env.DISCORD_CHANNEL_ID}/messages',
            params={'limit': 5},
            headers={
                'Authorization': f'Bot {env.DISCORD_TOKEN}',
                'Content-Type': 'application/json',
            },
        )

        if response.status_code == HTTPStatus.OK:
            messages = response.json()
            messages.reverse()
            for message in messages:
                result += f'{message['content']}\n'

        return result
