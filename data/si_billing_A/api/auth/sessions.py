"""Signature des cookies de session."""
import hashlib
import hmac

from .settings import SECRET_KEY


def sign_cookie(value: str) -> str:
    mac = hmac.new(SECRET_KEY, value.encode(), hashlib.sha1).hexdigest()
    return f"{value}.{mac}"


def verify_cookie(signed: str) -> bool:
    value, _, mac = signed.rpartition(".")
    expected = hmac.new(SECRET_KEY, value.encode(), hashlib.sha1).hexdigest()
    return hmac.compare_digest(mac, expected)
