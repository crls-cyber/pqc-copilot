"""Fonctions de hachage héritées."""
import hashlib


def legacy_checksum(data: bytes) -> str:
    """Somme de contrôle des anciens exports."""
    return hashlib.md5(data).hexdigest()
