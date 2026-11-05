# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Status

Empty skeleton: the files below exist but contain no code yet.

## Layout

- `app.py`: Streamlit chat UI
- `agent.py`: LLM loop (send messages, run tool calls, repeat until a text answer)
- `prompts.py`: system prompt
- `tools.py`: tool schemas + handlers
- `rules.py`: business rules (pure functions, no I/O)
- `db.py`: SQLite setup + seed data
- `tests/`: pytest; `conftest.py` holds shared fixtures

## Stack

- Python 3.13 with `uv` (`uv.lock` committed). Use `uv` / `make`, never bare `pip`.
- LLM through the `openai` SDK pointed at Fireworks: base URL `https://api.fireworks.ai/inference/v1`,
  key `FIREWORKS_API_KEY`, model `LLM_MODEL` (see `.env.example`). Read settings with `pydantic-settings`.
- Streamlit for the UI; SQLite for storage (`*.db` is git-ignored, so create the schema from code).

## Commands

```bash
make setup     # uv sync + pre-commit hooks
make run       # streamlit run app.py
make test      # pytest (excludes tests marked @pytest.mark.live)
make check     # ruff + pyright + pytest, same as CI
uv add <pkg>   # add a dependency
```

## Conventions

- Secrets only in `.env` / `.streamlit/secrets.toml` (git-ignored); pre-commit runs gitleaks.
- Business and safety rules live in code (`rules.py`, `tools.py`), not only in the prompt.
- Build file paths from the project folder, not the current working directory.
