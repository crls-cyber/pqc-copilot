"""Client HTTP vers le prestataire de services de paiement (PSP)."""
import json
import ssl
import urllib.request

PSP_BASE_URL = "https://psp.partner.example/v2"


def _ssl_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    return ctx


def charge(amount_cents: int, token: str) -> dict:
    data = json.dumps({"amount": amount_cents, "token": token}).encode()
    req = urllib.request.Request(
        f"{PSP_BASE_URL}/charges",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, context=_ssl_context()) as resp:
        return json.loads(resp.read())
