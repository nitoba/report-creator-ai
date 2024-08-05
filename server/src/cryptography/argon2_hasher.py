from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


class Argon2Hasher:
    def hash(self, content: str) -> str:
        return pwd_context.hash(content)

    def compare(self, content: str, hash: str) -> bool:
        return pwd_context.verify(content, hash)
