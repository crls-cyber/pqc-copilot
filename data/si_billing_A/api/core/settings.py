"""Paramètres de configuration de l'API de facturation."""
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://localhost/billing")
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
TOKEN_TTL_SECONDS = 3600

# Clé de repli utilisée lorsque l'environnement n'en fournit pas.
SECRET_KEY = bytes.fromhex("c3f1a9d8e7b64502c1d0a9f8e7b6c5d4")
