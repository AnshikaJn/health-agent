import os

LLM_BASE_URL = "https://api.fireworks.ai/inference/v1"
MODEL = os.environ.get("LLM_MODEL", "accounts/fireworks/models/qwen3p8-max")
MAX_STEPS = 5
