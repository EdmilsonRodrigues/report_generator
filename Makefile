.PHONY: lint
lint:
	ruff check src

.PHONY: format
format:
	ruff format
	ruff check src --fix
	ruff format
