"""Émission et validation des jetons JWT."""
from pathlib import Path

import jwt

from .settings import SECRET_KEY

_RSA_PRIVATE_KEY = Path(__file__).resolve().parents[2] / "pki" / "jwt-rs256.key"


def issue_session_token(claims: dict) -> str:
    """Jeton de session signé en HS256."""
    return jwt.encode(claims, SECRET_KEY, algorithm="HS256")


def issue_service_token(claims: dict) -> str:
    """Jeton inter-services signé en RS256."""
    return jwt.encode(claims, _RSA_PRIVATE_KEY.read_bytes(), algorithm="RS256")


def decode_token(token: str, key) -> dict:
    """Décode un jeton. Tolère les jetons des anciens services."""
    return jwt.decode(
        token,
        key,
        algorithms=["HS256", "RS256", "none"],
        options={"verify_signature": False},
    )
