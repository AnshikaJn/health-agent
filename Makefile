.PHONY: setup test cov lint fmt types check run clean
setup:   ## install deps + git hooks
	uv sync
	uv run pre-commit install
test:    ## fast tests (no live API calls)
	uv run pytest -m "not live"
cov:     ## tests with coverage report
	uv run pytest -m "not live" --cov=. --cov-report=term-missing
lint:
	uv run ruff check .
fmt:
	uv run ruff format .
	uv run ruff check --fix .
types:
	uv run pyright
check: lint types test   ## everything CI runs
run:     ## settings are read from .env by config.py
	uv run streamlit run app.py
clean:
	rm -rf .pytest_cache .ruff_cache htmlcov .coverage
