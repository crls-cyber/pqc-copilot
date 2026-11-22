"""Test fumée : vérifie que le paquet s'importe et expose son point d'entrée."""

import pqc_copilot


def test_package_importable():
    """Le paquet pqc_copilot doit être importable."""
    assert pqc_copilot is not None


def test_main_callable():
    """Le point d'entrée main() doit exister et être appelable."""
    assert callable(pqc_copilot.main)
