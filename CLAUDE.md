# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repo is a fresh `uv` scaffold — no commits yet, empty README, and `main.py` is still the generated
hello-world. There is no application architecture to preserve, so treat early structural decisions as open.
Keep this file updated as real modules land.

What the scaffold's config already commits to:

- **Python 3.13**, managed by `uv` (`uv.lock` is checked in — use `uv` commands, not bare `pip`/`python`).
- **LLM access via the `openai` SDK pointed at Fireworks**, not OpenAI: the only secret in `.env.example` is
  `FIREWORKS_API_KEY`. New code should construct the OpenAI client with Fireworks' `base_url`
  (`https://api.fireworks.ai/inference/v1`) and read the key through `pydantic-settings`, not `os.environ`
  directly.
- **Streamlit** as the UI layer, with `.streamlit/secrets.toml` gitignored.
- **SQLite** for persistence — `*.db` is gitignored, so schema must be creatable from code (migration/init
  routine), never restored from a committed file.

## Commands

```bash
uv sync                      # install/refresh env from uv.lock (incl. dev group)
uv run streamlit run main.py # run the app once a Streamlit entrypoint exists
uv run python main.py        # run the plain CLI entrypoint

uv run pytest                        # all tests
uv run pytest path/to/test_x.py::test_name  # single test
uv run ruff check . && uv run ruff format .  # lint + format
uv run pyright                       # type check
uv add <pkg> / uv add --dev <pkg>    # add a dependency (updates pyproject + lock)
```

`pre-commit` is a dev dependency but no `.pre-commit-config.yaml` exists yet; if you add hooks, mirror the
ruff/pyright/pytest commands above and run `uv run pre-commit install`.
