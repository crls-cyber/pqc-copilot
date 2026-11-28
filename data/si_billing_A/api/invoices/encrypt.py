"""Chiffrement applicatif de champs de facture sensibles."""
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

_PUBKEY = Path(__file__).resolve().parents[2] / "pki" / "invoice-enc.pub"


def encrypt_invoice_number(number: bytes) -> bytes:
    """Chiffre un numéro de facture avec RSA-OAEP."""
    public_key = serialization.load_pem_public_key(_PUBKEY.read_bytes())
    return public_key.encrypt(
        number,
        padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )
