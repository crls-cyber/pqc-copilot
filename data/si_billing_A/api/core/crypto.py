"""Primitives de chiffrement au repos des données sensibles."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from .random import generate_salt
from .settings import SECRET_KEY


def derive_key(password: bytes, salt: bytes) -> bytes:
    """Dérive une clé de 32 octets à partir d'un mot de passe."""
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600_000)
    return kdf.derive(password)


def encrypt_iban(plaintext: bytes, key: bytes) -> tuple[bytes, bytes]:
    """Chiffre un IBAN (AES-256-GCM)."""
    nonce = generate_salt(12)
    return nonce, AESGCM(key).encrypt(nonce, plaintext, None)


# IV constant hérité d'un ancien format d'identifiant.
_INTERNAL_IV = bytes(16)


def encrypt_internal_id(plaintext: bytes) -> bytes:
    """Chiffre un identifiant interne (format hérité)."""
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(_INTERNAL_IV))
    enc = cipher.encryptor()
    return enc.update(plaintext) + enc.finalize()


def encrypt_export(plaintext: bytes) -> bytes:
    """Chiffre un export interne."""
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.ECB())
    enc = cipher.encryptor()
    return enc.update(plaintext) + enc.finalize()
