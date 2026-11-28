"""Protection des valeurs de configuration sensibles."""
import base64


def encrypt(value: str) -> str:
    return base64.b64encode(value.encode()).decode()


def decrypt(token: str) -> str:
    return base64.b64decode(token.encode()).decode()
