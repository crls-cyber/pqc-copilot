# ===========================================================================
# Makefile — pqc-copilot
# Cibles principales imposées par le sujet : test, reproduce, reproduce-small
# Les commandes Python s'exécutent dans l'environnement uv (via « uv run »).
# ===========================================================================

.DEFAULT_GOAL := help

.PHONY: help install test reproduce reproduce-small clean

help:
	@echo "Cibles disponibles :"
	@echo "  make install          Installe l'environnement fige (uv sync)"
	@echo "  make test             Lance la suite de tests (pytest)"
	@echo "  make reproduce        Reconstruit results/ (pipeline complet)"
	@echo "  make reproduce-small  Version reduite pour la CI (petit modele)"
	@echo "  make clean            Supprime caches et artefacts regenerables"

install:
	uv sync

test:
	uv run pytest

reproduce:
	@echo ">>> reproduce : pipeline complet pas encore implemente (lots 1 a 4)"

reproduce-small:
	@echo ">>> reproduce-small : pipeline reduit pas encore implemente (lots 1 a 4)"

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
