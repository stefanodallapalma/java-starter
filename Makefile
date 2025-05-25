pre-commit-setup:
	git config --unset-all core.hooksPath || true
	pip3 install pre-commit || true
	pre-commit install || true

.PHONY: pre-commit-setup
