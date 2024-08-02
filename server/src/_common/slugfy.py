import re

from unidecode import unidecode


def create_slug(text: str) -> str:
    # Remove acentos
    texto_sem_acento = unidecode(text)
    # Converte para minúsculas
    texto_minusculas = texto_sem_acento.lower()
    # Remove caracteres especiais, mantendo apenas letras, números, espaços e hífens
    texto_limpo = re.sub(r'[^a-z0-9\s-]', '', texto_minusculas)
    # Substitui espaços por hífens
    slug = re.sub(r'[\s-]+', '-', texto_limpo).strip('-')
    return slug
