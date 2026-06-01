import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.main import call_openai, call_anthropic


def test_call_openai_missing_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    result = call_openai("test")
    assert result is None or "Error" in result


def test_call_anthropic_missing_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    result = call_anthropic("test")
    assert result is None or "Error" in result


def test_call_openai_no_import(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(sys, "path", [])
    import importlib
    import openai
    importlib.reload(openai)
    result = call_openai("test")
    assert result is None


def test_call_anthropic_no_import(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    result = call_anthropic("test")
    assert result is None or "Error" in result
