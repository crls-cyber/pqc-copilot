"""Empreintes des clés d'API."""
import hashlib


def fingerprint(api_key: str) -> str:
    """Empreinte stockée en base pour une clé d'API."""
    return hashlib.sha256(api_key.encode()).hexdigest()
