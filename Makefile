.PHONY: lint
lint:
	ruff check src

.PHONY: format
format:
	ruff format
	ruff check src --fix
	ruff format

.PHONY: static
static:
	mypy src/


.PHONY: test
test:
	pytest

.PHONY: e2e
e2e:


.PHONY: all
all: lint format static test
