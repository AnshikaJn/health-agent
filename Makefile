.PHONY: setup test cov lint fmt types check run clean
setup:   ## install deps + git hooks
	uv sync
	uv run pre-commit install
test:    ## fast tests (no live API calls); exit code 5 = "no tests yet", treated as OK
	uv run pytest -m "not live" || [ $$? -eq 5 ]
cov:     ## tests with coverage report
	uv run pytest -m "not live" --cov=. --cov-report=term-missing || [ $$? -eq 5 ]
lint:
	uv run ruff check .
fmt:
	uv run ruff format .
	uv run ruff check --fix .
types:
	uv run pyright
check: lint types test   ## everything CI runs
run:     ## loads .env into the environment
	uv run --env-file .env streamlit run app.py
clean:
	rm -rf .pytest_cache .ruff_cache htmlcov .coverage
