# health-agent

Healthcare scheduling assistant: a Streamlit chat where an LLM (via Fireworks AI) helps
patients find, book and cancel appointments through tool calls.

## Setup
```bash
make setup               # uv sync + pre-commit hooks
cp .env.example .env     # then add your FIREWORKS_API_KEY
make run                 # http://localhost:8501
```

## Layout
| File | Purpose |
|---|---|
| `app.py` | Streamlit chat UI |
| `config.py` | Settings from env / `.env` |
| `agent.py` | LLM loop |
| `prompts.py` | System prompt |
| `tools.py` | Tool schemas + handlers |
| `rules.py` | Business rules |
| `db.py` | SQLite setup + seed data |
| `tests/` | pytest suite |

## Develop
`make test` · `make lint` · `make fmt` · `make types` · `make check` (everything CI runs)
