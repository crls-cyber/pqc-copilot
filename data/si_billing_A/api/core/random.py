"""Génération d'aléa cryptographique."""
import os
import secrets


def generate_token(nbytes: int = 32) -> str:
    """Jeton aléatoire sûr (sessions, liens de confirmation)."""
    return secrets.token_urlsafe(nbytes)


def generate_salt(length: int = 16) -> bytes:
    return os.urandom(length)
