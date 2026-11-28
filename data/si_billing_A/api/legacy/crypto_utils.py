"""Utilitaires de chiffrement hérités (format d'archive V1)."""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def _legacy_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    enc = cipher.encryptor()
    return enc.update(data) + enc.finalize()
