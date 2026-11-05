import importlib

import pytest
from pydantic import ValidationError

from config import Settings


@pytest.mark.parametrize("module", ["app", "agent", "prompts", "tools", "rules", "db", "config"])
def test_modules_import(module: str) -> None:
    importlib.import_module(module)


def test_settings_reads_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FIREWORKS_API_KEY", "fake-key")
    monkeypatch.setenv("LLM_MODEL", "some/model")
    s = Settings(_env_file=None)  # pyright: ignore[reportCallIssue]  # ignore the real .env
    assert s.fireworks_api_key.get_secret_value() == "fake-key"
    assert s.llm_model == "some/model"
    assert "fake-key" not in repr(s)  # SecretStr keeps the key out of logs


def test_settings_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("FIREWORKS_API_KEY", raising=False)
    with pytest.raises(ValidationError):
        Settings(_env_file=None)  # pyright: ignore[reportCallIssue]
